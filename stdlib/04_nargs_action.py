"""
std.f0.01d — nargs vs action, grupy argumentow, --help jako dokumentacja

Roznica, ktora trzeba miec w glowie:

  nargs  = ILE wartosci pobiera JEDNO wystapienie argumentu
  action = CO argparse robi, gdy argument sie pojawi

Dlatego `--tag a --tag b` (action='append') to co innego niz
`--tag a b` (nargs='+'). Pierwsze zbiera przez powtorzenia, drugie za jednym razem.

Zrodlo: przyklady wygenerowane przez Copilota (_copilot/), okrojone do istoty
i poprawione — w oryginale `const` siedzial na argumencie pozycyjnym, gdzie
nigdy sie nie odpala (patrz komenda `report` nizej).
"""

import argparse
from pathlib import Path


def existing_file(s):
    p = Path(s)
    if not p.exists():
        raise argparse.ArgumentTypeError(f"plik nie istnieje: {s}")
    return p


def pokaz(args):
    print(f"  args = {args}")


def cmd_batch(args):
    print(f"batch: {len(args.files)} plikow")
    for f in args.files:
        print(f"   - {f}")
    print(f"   tagi: {args.tags or '(brak)'}")
    print(f"   dry-run: {args.dry_run}")
    pokaz(args)


def cmd_transform(args):
    print(f"transform: {args.input or 'STDIN'}")
    print(f"   reguly: {args.rules if args.rules is not None else '(brak flagi)'}")
    print(f"   poziom -v: {args.verbose}")
    pokaz(args)


def cmd_report(args):
    print(f"report -> {args.output or 'STDOUT'}")
    print(f"   sekcje: {args.include or '(wszystkie)'}")
    pokaz(args)


def build_parser():
    p = argparse.ArgumentParser(
        prog='mycli',
        description='nargs vs action',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--format', choices=['json', 'text', 'csv'], default='text')

    sub = p.add_subparsers(dest='cmd', required=True)

    # ── batch: nargs='+' na pozycyjnym, action='append' i 'store_true' ──
    b = sub.add_parser('batch', help='przetworz wiele plikow', parents=[common])
    b.add_argument('files', nargs='+', type=existing_file,
                   help='pliki (min. 1) — nargs=+ zbiera je za JEDNYM wystapieniem')
    b.add_argument('--tag', action='append', dest='tags',
                   help='tag; POWTARZALNY: --tag a --tag b')
    b.add_argument('--dry-run', action='store_true', help='tylko podglad')
    b.set_defaults(fn=cmd_batch)

    # ── transform: nargs='?' i '*', action='count' ──
    t = sub.add_parser('transform', help='transformuj dane', parents=[common])
    t.add_argument('input', nargs='?', type=existing_file, default=None,
                   help='plik wejscia; nargs=? -> 0 albo 1')
    t.add_argument('--rule', nargs='*', dest='rules',
                   help="reguly; nargs=* -> --rule bez wartosci daje PUSTA liste, "
                        "brak flagi daje None (to nie to samo)")
    t.add_argument('--verbose', '-v', action='count', default=0,
                   help='poziom: -v=1, -vv=2, -vvv=3')
    t.set_defaults(fn=cmd_transform)

    # ── report: nargs='?' + const NA OPCJI (tam const dziala) ──
    r = sub.add_parser('report', help='generuj raport', parents=[common])
    r.add_argument('--output', nargs='?', const='report.txt', default=None,
                   help='brak flagi -> STDOUT; --output bez wartosci -> report.txt; '
                        '--output x.txt -> x.txt')
    # grupa istnieje TYLKO po to, by --help mial sekcje. Nie zmienia parsowania.
    sekcje = r.add_argument_group('zawartosc raportu')
    sekcje.add_argument('--include', action='append', help='sekcja do wlaczenia')
    sekcje.add_argument('--quiet', '-q', action='store_true', help='bez komunikatow')
    r.set_defaults(fn=cmd_report)

    return p


def main():
    args = build_parser().parse_args()
    args.fn(args)


if __name__ == '__main__':
    main()
