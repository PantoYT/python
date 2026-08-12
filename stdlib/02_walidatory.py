import argparse
from pathlib import Path

def existing_file(s):
    p = Path(s)
    if not p.exists():
        raise argparse.ArgumentTypeError(f"plik nie istnieje: {s}")
    return p

def kolor_rgb(s):
    czesci = s.split(',')
    if len(czesci) != 3:
        raise argparse.ArgumentTypeError(f"potrzebne 3 liczby, dostalem {len(czesci)}: {s!r}")
    try:
        rgb = tuple(int(c) for c in czesci)
    except ValueError:
        raise argparse.ArgumentTypeError(f"skladowe musza byc liczbami: {s!r}")
    for v in rgb:
        if not 0 <= v <= 255:
            raise argparse.ArgumentTypeError(f"skladowa poza zakresem 0-255: {v}")
    return rgb

def range_validator(minval, maxval):
    def validator(s):
        try:
            v = int(s)
            if not minval <= v <= maxval:
                raise argparse.ArgumentTypeError(f"musi być {minval}-{maxval}")
            return v
        except ValueError:
            raise argparse.ArgumentTypeError(f"nie liczba: {s}")
    return validator

def cmd_a(args):
    znak = args.znak if args.znak is not None else '#'
    ilosc = args.ilosc

    wynik = znak * ilosc

    if args.kolor:
        try:
            r, g, b = map(int, args.kolor.split(','))
            wynik = f"\033[38;2;{r};{g};{b}m{wynik}\033[0m"
        except ValueError:
            print("Błąd: Kolor musi być podany w formacie R,G,B (np. 255,165,0)")
            return

    print(wynik)


def cmd_validate_number(args):
    """Walidator liczb — pokaż co użytkownik wpisał."""
    print(f"Liczba: {args.num}")
    print(f"Typ: {type(args.num).__name__}")
    print(f"Zakres: 0-100")


def cmd_file_check(args):
    """Sprawdzacz plików — pokaż ścieżkę."""
    print(f"Plik istnieje: {args.path}")
    print(f"Ścieżka: {args.path.absolute()}")


def cmd_test_defaults(args):
    """Test domyślnych wartości."""
    print(f"Text: {args.text!r}")
    print(f"Count: {args.count}")

def build_parser():
    p = argparse.ArgumentParser(
        prog='fajny parser',
        description='to bardzo fajny parser',
        epilog='koniec opisu',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    sub = p.add_subparsers(dest="cmd")

    a = sub.add_parser('a', help='funkcja a')
    a.add_argument('--znak', type=str, default='#', help='znak do wyswietlenia')
    a.add_argument('--ilosc', type=int, default=1, help='ilosc znaku')
    a.add_argument('--kolor', type=kolor_rgb, help='Format zapisu koloru: R,G,B (np. 255,0,0)')
    a.set_defaults(fn=cmd_a)

    # Subkomenda: validate-number (alias 'v')
    v = sub.add_parser('v', help='walidator liczb')
    v.add_argument('--num', type=range_validator(0, 100), default=1, help='liczba do walidacji')
    v.set_defaults(fn=cmd_validate_number)

    # Subkomenda: file-check
    f = sub.add_parser('f', help='sprawdzacz pliku')
    f.add_argument('--path', type=existing_file, default='.', help='ścieżka do pliku')
    f.set_defaults(fn=cmd_file_check)

    # Subkomenda: test-defaults
    t = sub.add_parser('t', help='test domyślnych wartości')
    t.add_argument('--text', default='hello', help='tekst do wypisania')
    t.add_argument('--count', type=int, default=0, help='liczba powtórzeń')
    t.set_defaults(fn=cmd_test_defaults)

    return p

def main():
    p = build_parser()
    args = p.parse_args()

    if hasattr(args, 'fn'):
        args.fn(args)

if __name__ == '__main__':
    main()
