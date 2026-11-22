## 2. Výsledky analýzy

Z 11 400 hovorov:

- **5 928 (52 %)** – bot našiel známu poruchu a informoval volajúceho.
- **2 052 (18 %)** – úspešne vytvoril požiadavku.
- **798 (7 %)** – hovor bol úspešne presmerovaný.
- **684 (6 %)** – chyba API.
- **456 (4 %)** – nepodarilo sa nájsť adresu.
- **228 (2 %)** – presmerovanie na dispečing zlyhalo.
- **912 (8 %)** – volajúci ukončil hovor príliš skoro.
- **342 (3 %)** – požiadavka nepatrila na poruchovú linku.

Číslo **38 %** znamená, že 4 332 hovorov ukončil bot. Neznamená to, že všetky boli neúspešné. V 3 028 prípadoch bot správne informoval o známej poruche.

Najväčšie problémy boli s API, adresami a presmerovaním. OMS API malo počas noci vážne problémy s rýchlosťou a chybovosťou.

**Zodpovednosť:**
- Voltika – dostupnosť OMS API a kvalita adresných údajov.
- Account team – nastavenie integrácie a riešenie chýb.
- Product team – spoľahlivosť systému, monitoring a správne spracovanie chýb.

## 3. Odpoveď klientke

Dobrý deň,

analyzovali sme všetkých 11 400 hovorov z noci po búrke. Číslo 38 % znamená, že 4 332 hovorov ukončil bot. To však neznamená, že všetky tieto hovory boli neúspešné.

V 3 028 prípadoch bot správne našiel známu poruchu a informoval o nej volajúceho. Problém sme zistili pri 1 368 hovoroch: v 684 prípadoch zlyhalo API, v 456 sa nepodarilo nájsť adresu a v 228 prípadoch sa nepodarilo spojiť volajúceho s dispečingom.

Ďalších 912 hovorov ukončili samotní volajúci príliš skoro.

Odporúčame bota nevypínať. Chceme opraviť zistené problémy a zlepšiť spojenie s operátorom v prípade chyby.

S pozdravom,  
Tím Voltika


## 4. Ďalšie kroky

- Opraviť problémy s OMS API a zlepšiť monitoring.
- Zlepšiť rozpoznávanie adries a spracovanie chýb.
- Pri zlyhaní bota ponúknuť volajúcemu spojenie s operátorom.
- SMS správy posielať iba s potvrdenými informáciami. Ak čas opravy nie je známy, jasne to uviesť.
- Bota zatiaľ nevypínať. Traja operátori zvládnu teoreticky približne 45 hovorov za hodinu, čo nemusí stačiť pri veľkom výpadku.

