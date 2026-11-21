import json
from collections import Counter



def load_calls(path):
    call_list = []
    with open(path) as file:
        for line in file:
            res = json.loads(line)
            call_list.append(res)
            
    return call_list

            
calls = load_calls("data/labeled_sample.jsonl")

label_counts = Counter(call["label"] for call in calls)

for label, count in label_counts.most_common():
    print(f"{label}: {count}")

    event_types = Counter(
    event["type"]
    for call in calls
    for event in call["events"]
)

print("Event types:")
for event_type, count in event_types.most_common():
    print(f"{event_type}: {count}")

tool_calls = Counter()
tool_results = Counter()

for call in calls:
    for event in call["events"]:
        if event["type"] == "tool_call":
            tool_calls[event.get("tool", "UNKNOWN")] += 1

        elif event["type"] == "tool_result":
            key = (
                event.get("tool", "UNKNOWN"),
                event.get("status", "UNKNOWN")
            )
            tool_results[key] += 1

print("Tool calls:")
for tool, count in tool_calls.most_common():
    print(tool, count)

print("\nTool results:")
for (tool, status), count in tool_results.most_common():
    print(f"{tool} | {status}: {count}")