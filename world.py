def check(mul):
    div=100/mul
    ro=round(div,2)
    if ro<9.58:
        return "yes"
    return "no"




def multi(a,b,c,v):
    return a*b*c*v





test=int(input())
for i in range(test):
    a,b,c,v=[float(x) for x in input().split()]
    mul=multi(a,b,c,v)
    print(check(mul))
