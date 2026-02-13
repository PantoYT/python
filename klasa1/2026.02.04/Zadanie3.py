def czy_poprawna_pora(g,m):
    if g >= 0 and g < 24 and m >= 0  and m < 60:
        return True
    return False

def ile_minut(g,m):
    return m+g*60

print(czy_poprawna_pora(23,59))
print(ile_minut(23,59))