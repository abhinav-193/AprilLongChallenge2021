def check(a,b,c):
    if a==b or b==c or c==a:
        return "yes"
    else:
        return "no"







a,b,c=[int(x) for x in input().split()]
print(check(a,b,c))
