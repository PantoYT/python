import argparse

def cmd_a(args):
    znak = args.znak if args.znak else '#'
    ilosc = args.ilosc if args.ilosc else 1

    wynik = znak * ilosc

    if args.kolor:
        try:
            r, g, b = map(int, args.kolor.split(','))
            wynik = f"\033[38;2;{r};{g};{b}m{wynik}\033[0m"
        except ValueError:
            print("Błąd: Kolor musi być podany w formacie R,G,B (np. 255,165,0)")
            return

    print(wynik)




def build_parser():
    p = argparse.ArgumentParser(prog='fajny parser',description='to bardzo fajny parser',epilog='koniec opisu')
    sub = p.add_subparsers(dest="cmd")

    a = sub.add_parser('a', help='funkcja a')
    a.add_argument('--znak', type=str, help='znak do wyswietlenia')
    a.add_argument('--ilosc', type=int, help='ilosc znaku')
    a.add_argument('--kolor', type=str, help='Format zapisu koloru: R,G,B (np. 255,0,0)')
    a.set_defaults(fn=cmd_a)

    return p

def main():
    p = build_parser()
    args = p.parse_args()

    if hasattr(args, 'fn'):
        args.fn(args)

if __name__ == '__main__':
    main()
