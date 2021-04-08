def check(string,k):
    count=0
    li=[x for x in string]
    i=0
    while i<len(li):
        s=0
        count=0
        if li[i]=='*':
            while i<len(li) and li[i]=="*":
                count=count+1
                i=i+1
                s=1
        if count==k:
            return "yes"
        if s==0:
            i=i+1
    return "no"







test=int(input())
for i in range(test):
    n,k=[int(x) for x in input().split()]
    string=input()
    print(check(string,k))
