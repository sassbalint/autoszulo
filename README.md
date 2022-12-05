# autoszulo

Segítség azoknak a szülőknek, akik összes gyermekük tekintetében egy gombnyomással szeretnék kitölteni a [BM-es szülői kérdőívet](https://szuloikerdoiv1.unipoll.hu/PagesForResponse/normalsurvey/response?surveyid=20124780) úgy, hogy a kérdéseket üresen hagyják és a szöveges javaslatba a [9 követelést](https://szuloihang.hu/kretakerdoiv) írják be. :heart:

## > windows <

### előkészítés

1. [Töltse le az `autoszulo.py` programot](https://raw.githubusercontent.com/sassbalint/autoszulo/main/autoszulo.py) :arrow_left: ide katt jobbgomb + "Hivatkozás mentése más néven..."...
2. ...és mentse el az Asztalra `autoszulo.py` néven, a "Fájl típusa" legyen "Minden fájl".
3. A Startmenü "Keresés" mezőjébe írja be: `cmd`, majd kattintson a megjelenő "Parancssor" alkalmazásra.
4. A megjelenő fekete ablakba írja be: `cd Desktop` + Enter.
5. Írja be: `autoszulo.py` + Enter.
6. A megjelenő ablakban válassza az "Alkalmazás keresése a Microsoft Store-ben" lehetőséget + OK. Ha nem jelenik meg ilyen ablak, akkor folytassa a 8. pontnál.
7. Katt a "Python 3.10"-re + jobb fent katt a "Beszerzés"-re, várja meg míg települ a Python.
8. Térjen vissza a `cmd` ablakába és írja be: `pip install selenium webdriver_manager` + Enter, várja meg míg lefut a szükséges kiegészítő modulok telepítése.

### használat
Írja be a `cmd` ablakába: `python3 autoszulo.py` + Enter.

Néhány másodpercen belül elkezd működni a dolog :tada:, a képernyőn láthatjuk, hogy hogyan tölti ki a rendszer a kérdőívet.
A program alapból három gyermekre tölti ki a kérdőívet, a kitöltések között néhány másodperc szünet van.

Ha Önnek esetleg ettől eltérő számú gyermeke van, akkor a gyermekek számát az `-n` kapcsolóval adhatja meg:
Négy gyermek esetén például ezt írja be a `cmd` ablakába: `python3 autoszulo.py -n 4` + Enter.

### rendszerkövetelmények

Firefox szükséges hozzá. Meg Python, de azt a fentiek során telepítjük, ha esetleg nem lenne.
Tesztelve: Windows 11 Pro-n.

## > linux <

### előkészítés

```python
git clone https://github.com/sassbalint/autoszulo
cd autoszulo
pip install -r requirements.txt
```

### használat

```python
python3 autoszulo.py
```

A program alapból három gyermekre tölti ki a kérdőívet.
Ha Önnek esetleg ettől eltérő számú gyermeke van, akkor a gyermekek számát megadhatja a `-n` kapcsolóval.
Például négy gyermek esetén:

```python
python3 autoszulo.py -n 4
```

### rendszerkövetelmények

Firefox szükséges hozzá. Meg Python, de az úgyis van.
Tesztelve: Ubuntu 18.04-en.
