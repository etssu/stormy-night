# NOTES

- **Predpoklady:** Úspešný výsledok API považujem za úspešný iba vtedy, keď ho potvrdzuje aj ďalší priebeh hovoru.
- **Čo by som urobila s viac časom:** Otestovala by som klasifikátor na väčšej vzorke hovorov.
- **Použitie AI:** AI mi pomohla s kontrolou logiky a formuláciou výsledkov.
- **Delegovanie:** AI som využila ako pomocníka pri analýze a písaní.
- **Čo som skontrolovala:** Výsledky klasifikácie, počet hovorov a vytvorený CSV súbor.
- **Chyba AI:** AI navrhla zbytočne podrobnú analýzu hovorov, ktorá nebola potrebná na základné vyhodnotenie.
- **Čo som vedome nerobila:** Nepokúšala som sa automaticky priradiť všetky chyby API k jednému problému OMS, pretože dostupné metriky nepotvrdzujú príčinu každej chyby.

## Spustenie

Klasifikátor spustím príkazom:

```bash
python classify.py input.jsonl output.csv
```