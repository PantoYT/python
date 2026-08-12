"""
std.f0.01c — wiele subkomend i wspolne flagi przez parents=

Kluczowa rzecz: `common` to ZWYKLY ArgumentParser z add_help=False.
Nie jest uruchamiany — sluzy tylko jako pojemnik na argumenty,
ktore doklejaja sie do kazdej subkomendy przez parents=[common].

Bez add_help=False dostaniesz konflikt: dwa razy -h w tej samej subkomendzie.

Zrodlo: przyklady wygenerowane przez Copilota (_copilot/), okrojone do istoty.
Kod cmd_a / kolor_rgb / existing_file jest moj, z 02_walidatory.py.
"""

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


def pokaz(args):
    """Najwazniejsza linijka w calym pliku: zobacz, co naprawde dostales."""
    print(f"  args = {args}")


def cmd_a(args):
    znak = args.znak
    wynik = znak * args.ilosc
    if args.kolor:
        r, g, b = args.kolor          # type= juz zwrocil krotke, nic nie parsujemy
        wynik = f"\033[38;2;{r};{g};{b}m{wynik}\033[0m"
    print(wynik)
    if args.verbose:
        pokaz(args)


def cmd_process(args):
    print(f"process: {args.input} -> {args.output} (format {args.format})")
    if args.verbose:
        pokaz(args)


def cmd_analyze(args):
    print(f"analyze: {args.file} (deep={args.deep}, format={args.format})")
    if args.verbose:
        pokaz(args)


def build_parser():
    p = argparse.ArgumentParser(
        prog='mycli',
        description='wspolne flagi przez parents=',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # RODZIC: sam nigdy nie parsuje, tylko uzycza swoich argumentow
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--verbose', '-v', action='store_true', help='pokaz namespace')
    common.add_argument('--format', choices=['json', 'text', 'csv'], default='text',
                        help='format wyjscia')

    # required=True: brak subkomendy = blad z usage, zamiast cichego wyjscia
    sub = p.add_subparsers(dest='cmd', required=True)

    a = sub.add_parser('a', help='koloruj znak', parents=[common],
                       formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    a.add_argument('--znak', default='#', help='znak do wyswietlenia')
    a.add_argument('--ilosc', type=int, default=1, help='ilosc znaku')
    a.add_argument('--kolor', type=kolor_rgb, help='R,G,B (np. 255,0,0)')
    a.set_defaults(fn=cmd_a)

    pr = sub.add_parser('process', help='przetworz plik', parents=[common],
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    pr.add_argument('--input', type=existing_file, required=True, help='plik wejsciowy')
    pr.add_argument('--output', default='output.txt', help='plik wyjsciowy')
    pr.set_defaults(fn=cmd_process)

    an = sub.add_parser('analyze', help='przeanalizuj plik', parents=[common],
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    an.add_argument('--file', type=existing_file, required=True, help='plik do analizy')
    an.add_argument('--deep', action='store_true', help='glebsza analiza')
    an.set_defaults(fn=cmd_analyze)

    return p


def main():
    args = build_parser().parse_args()
    args.fn(args)          # required=True gwarantuje, ze fn istnieje


if __name__ == '__main__':
    main()
