def min2(a,b):
    if a < b: return a
    else: return b   

def max2(a,b):
    if a > b: return a
    else: return b

def min3(a,b,c):
    smol=min2(a,b)
    return min2(smol,c)

def max3(a,b,c):
    big=max2(a,b)
    return max2(big,c)

def minmaxlist(list):
    max=list[0]
    min=list[0]
    for i in range(1,len(list)):
        if list[i] > max: max = list[i]
        if list[i] < min: min = list[i]
    return min,max

print(min2(5,7))
print(max2(93,9))
print(min3(5,7,1))
print(max3(93,9,100))

print(minmaxlist([1,3,5,7,13,65,111,86,123123,15,-1,-83,999999]))

# for larger sets convert to a list, get min and max that way, don't hard-code