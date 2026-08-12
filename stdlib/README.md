# stdlib — cwiczenia do tracku `stdlib` w ZNEK

Checkpointy. Kazdy plik to jeden etap i **zostaje nietkniety** — nowy etap to nowy
plik, nie edycja poprzedniego.

| plik | task | czyj kod | stan |
|---|---|---|---|
| `01_pierwsza.py` | `std.f0.01` | moj | zrobione |
| `02_walidatory.py` | `std.f0.01b` | moj | **2 poprawki do zrobienia** |
| `03_parents.py` | `std.f0.01c` | Copilot, okrojony | do przerobienia samemu |
| `04_nargs_action.py` | `std.f0.01d` | Copilot, okrojony + poprawiony | do przerobienia samemu |

03 i 04 sa **materialem, nie moim osiagnieciem**. Zanim je uznam za zaliczone,
pisze wlasna wersje od zera i dopiero potem porownuje.

## Do zrobienia w `02_walidatory.py`

1. **Crash na `--kolor 255,0,0`.** `type=kolor_rgb` zwraca krotke, a `cmd_a` nadal
   robi `args.kolor.split(',')` -> `AttributeError`. Caly blok `try/except` jest
   martwy, zastapic: `r, g, b = args.kolor`.
2. **`formatter_class` nie schodzi do subkomend.** Ustawiony tylko na parserze
   glownym, a argumenty siedza na subparserach — `--help` subkomendy nie pokazuje
   domyslnych. Podac przy kazdym `add_parser` (patrz `03_parents.py`).

```
python 02_walidatory.py a --znak X --ilosc 3 --kolor 255,0,0
python 02_walidatory.py t --help
```

## Co pokazuja 03 i 04

**`03_parents.py`** — `common = ArgumentParser(add_help=False)` jako pojemnik na
wspolne flagi, doklejany przez `parents=[common]`. Bez `add_help=False` bedzie
konflikt dwoch `-h`. Do tego `choices=`, `required=True` na argumencie i
`required=True` na subparserach (brak subkomendy = blad z usage, zamiast cichego
wyjscia z kodem 0, jak w `01_pierwsza.py`).

**`04_nargs_action.py`** — roznica, o ktora chodzi w tym tasku:

```
nargs  = ILE wartosci pobiera JEDNO wystapienie argumentu
action = CO argparse robi, gdy argument sie pojawi
```

Zweryfikowane odpaleniem:

| komenda | wynik |
|---|---|
| `batch f1 f2 --tag rel --tag pilne` | `files=[f1, f2]`, `tags=['rel','pilne']` |
| `transform -vvv` | `verbose=3` (`action='count'`) |
| `transform --rule` | `rules=[]` — pusta lista |
| `transform` | `rules=None` — **to nie to samo** |
| `report` | STDOUT |
| `report --output` | `report.txt` (z `const`) |
| `report --output x.txt` | `x.txt` |

Plus `add_argument_group('zawartosc raportu')` — nie zmienia parsowania, robi tylko
sekcje w `--help`. To jest ta czesc, ktora sprawia, ze `--help` czyta sie jak
dokumentacja.

Poprawka wzgledem oryginalu Copilota: mial `const=` na argumencie **pozycyjnym**,
gdzie nigdy sie nie odpala. `const` dziala tylko na opcji z `nargs='?'`, gdy flaga
jest podana bez wartosci.

## Czego tu juz nie ma

Katalog `_copilot/` (9 plikow) — skasowany, wartosciowe fragmenty przeszly do 03 i 04.

Copilot mial odtworzyc moje wczesniejsze wersje z historii czatu i tego nie zrobil:
`cmd_test_defaults` z mojej drugiej wersji nie wystepowal w zadnym z tych plikow,
a `mycli_v1_twoj.py` zawieral `type=lambda s: ...`, ktorego nigdy nie napisalem.
Model rekonstruowal kod, zamiast go odczytac.

**Wniosek:** wersja, ktora ma przetrwac, musi lezec w pliku. Stad numeracja wyzej.

## Pulapka, ktora tu byla

W `__pycache__` lezal `argparse.cpython-314.pyc` — czyli istnial tu kiedys plik
`argparse.py`. Wtedy `import argparse` wciaga **moj** plik zamiast biblioteki
standardowej i bledy przestaja miec sens. Nigdy nie nazywac pliku tak, jak modul,
ktory sie importuje: `argparse.py`, `json.py`, `random.py`, `socket.py`, `email.py`.
