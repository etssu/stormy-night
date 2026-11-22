import csv
import json
from collections import Counter


def load_calls(path):
    call_list = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            call_list.append(json.loads(line))

    return call_list


def classify_call(call):
    events = call["events"]

    # Successfully created ticket
    for event in events:
        if (
            event.get("type") == "tool_result"
            and event.get("name") == "create_ticket"
            and event.get("status") == "ok"
        ):
            result = event.get("result") or {}

            if result.get("ticket_id"):
                return "TICKET_CREATED"
            
    # Transfer result
    for event in events:
        if event.get("type") == "transfer":
            status = event.get("status")

            if status == "connected":
                return "TRANSFERRED"

            if status in ("timeout", "queue_full"):
                return "TRANSFER_FAILED"

    # Known outage informed
    for event in events:
        if (
            event.get("type") == "tool_result"
            and event.get("name") == "get_outage"
            and event.get("status") == "ok"
        ):
            result = event.get("result") or {}

            if result.get("outage_id"):
                outage_time = event["t"]

                informed = False

                for e in events:
                    if e.get("type") == "hangup" and e.get("by") == "caller":
                        if e.get("t", 0) >= outage_time:
                            break

                    if (
                        e.get("type") == "bot"
                        and e.get("t", 0) >= outage_time
                        and "evidujeme poruchu" in e.get("text", "").lower()
                    ):
                        informed = True
                        break

                if informed:
                    return "KNOWN_OUTAGE_INFORMED"

    # API error
    for event in events:
        if (
            event.get("type") == "tool_result"
            and event.get("name") in ("get_outage", "create_ticket")
            and event.get("status") in ("timeout", "error")
        ):
            return "API_ERROR"

    # API request without a result
    for event in events:
        if (
            event.get("type") == "tool_call"
            and event.get("name") in ("get_outage", "create_ticket")
        ):
            tool_name = event["name"]
            call_time = event["t"]

            has_result = any(
                e.get("type") == "tool_result"
                and e.get("name") == tool_name
                and e.get("t", 0) >= call_time
                for e in events
            )

            caller_hangup = any(
                e.get("type") == "hangup"
                and e.get("by") == "caller"
                and e.get("t", 0) > call_time
                for e in events
            )

            if not has_result and caller_hangup:
                return "API_ERROR"

    # Out of scope
    for event in events:
        if (
            event.get("type") == "route"
            and event.get("target") == "customer_line"
        ):
            return "OUT_OF_SCOPE"

    # Address not understood
    for event in events:
        if (
            event.get("type") == "bot"
            and "adresu sa mi nepodarilo nájsť" in event.get("text", "").lower()
        ):
            return "ADDRESS_NOT_UNDERSTOOD"

    # Ended early
    caller_hangups = [
        e for e in events
        if e.get("type") == "hangup" and e.get("by") == "caller"
    ]

    if caller_hangups:
        hangup_time = caller_hangups[0]["t"]

        if not any(
            e.get("type") == "bot"
            and e.get("t", 0) > hangup_time
            for e in events
        ):
            return "ENDED_EARLY"
        
    return "UNKNOWN"

# Load full dataset
calls = load_calls("data/transcripts.jsonl")

# Classify all calls
predictions = [
    (call["call_id"], classify_call(call))
    for call in calls
]

# Save predictions to CSV
with open("predictions_night1.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["call_id", "label"])
    writer.writerows(predictions)

# Validate output
labels = Counter(label for _, label in predictions)
call_ids = [call_id for call_id, _ in predictions]

print("Total predictions:", len(predictions))
print("Unique call IDs:", len(set(call_ids)))
print("Predicted labels:", labels)
print("UNKNOWN:", labels.get("UNKNOWN", 0))
print("CSV created: predictions_night1.csv")

