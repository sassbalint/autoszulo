# autoszulo

Segítség azoknak a szülőknek, akik összes gyermekük tekintetében egy gombnyomással szeretnék kitölteni a [BM-es szülői kérdőívet](https://szuloikerdoiv1.unipoll.hu/PagesForResponse/normalsurvey/response?surveyid=20124780) úgy, hogy a kérdéseket üresen hagyják és a szöveges javaslatba a [9 követelést](https://szuloihang.hu/kretakerdoiv) írják be. :heart:

## > windows <

### előkészítés
[Töltse le az `autoszulo.exe` programot](https://github.com/sassbalint/autoszulo/releases/download/latest/autoszulo.exe) :arrow_left: ide kattintva.

### használat
Kattintson a letöltött `autoszulo.exe` programra.
Ha azt az üzenetett kapja, hogy
"A Windows megvédte a számítógépét" vagy hasonlót,
akkor kattintson a "További információ"-ra,
majd a "Futtatás mindenképpen"-re.

Ekkor a program megkérdezi,
hogy hány gyermekre töltse ki a kérdőívet.
Ha nem ad meg semmit, akkor alapból 3 gyermekre fogja kitölteni.
Utána a program bekéri azt a linket,
amit a Krétában kapott a kérdőívhez.
Ha ezt nem adja meg, akkor a
[`444.hu` oldalán közzétett linket](https://444.hu/2022/12/02/atneztuk-a-belugy-szuloi-elegedettseg-kerdoivet-nem-vagyunk-elegedettek) fogja használni.

Az "OK" megnyomását követő néhány másodpercen belül elkezd működni a dolog :tada:, a képernyőn láthatjuk, hogy hogyan tölti ki a rendszer a kérdőívet.

### rendszerkövetelmények

Firefox szükséges hozzá. Tesztelve: Windows 11 Pro-n.

## > linux <

### előkészítés

```python
git clone https://github.com/sassbalint/autoszulo
cd autoszulo
pip install -r requirements.txt
```

### használat

```python
python3 autoszulo.py -l "LINK"
```

A `LINK` helyén azt a linket szükséges megadni,
amit a Krétában kapott a kérdőívhez.
Ha ezt nem adja meg, akkor a
[`444.hu` oldalán közzétett linket](https://444.hu/2022/12/02/atneztuk-a-belugy-szuloi-elegedettseg-kerdoivet-nem-vagyunk-elegedettek) fogja használni a program.

A program alapból három gyermekre tölti ki a kérdőívet.
Ha ettől eltérő számú gyermekre szeretné kitölteni, akkor a gyermekek számát megadhatja a `-n` kapcsolóval.
Például négy gyermek esetén:

```python
python3 autoszulo.py -n 4
```

### rendszerkövetelmények

Firefox szükséges hozzá. Meg Python, de az úgyis van.
Tesztelve: Ubuntu 18.04-en.
