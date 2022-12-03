# autoszulo

Segítség azoknak a szülőknek, akik összes gyermekük tekintetében egy gombnyomással szeretnék kitölteni a [BM-es szülői kérdőívet](https://szuloikerdoiv1.unipoll.hu/PagesForResponse/normalsurvey/response?surveyid=20124780) úgy, hogy a kérdéseket üresen hagyják és a szöveges javaslatba a [9 követelést](https://szuloihang.hu/kretakerdoiv) írják be.

## installálás

```python
pip install -r requirements.txt
```

## használat

```python
python3 autoszulo.py
```

A program alapból három gyermekre tölti ki a kérdőívet.
Ha Önnek esetleg ettől eltérő számú gyermeke van, akkor a gyermekek számát megadhatja a `-n` kapcsolóval.
Például négy gyermek esetén:

```python
python3 autoszulo.py -n 4
```

## rendszerkövetelmények

Python3 szükséges hozzá meg Firefox.
Tesztelve: ubuntu 18.04-en.
Biztos megy windows-on is valahogy.
