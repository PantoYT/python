def min2(a,b):
    if a < b: return a
    else: return b   

def max2(a,b):
    if a > b: return a
    else: return b

def min3(a,b,c):
    if a < b:
        if a < c: return a
        else: return c
    else: 
        if b < c: return b
        else: return c

def max3(a,b,c):
    if a > b:
        if a > c: return a
        else: return c
    else: 
        if b > c: return b
        else: return c

# for larger sets convert to a list, get min and max that way, don't hard-code