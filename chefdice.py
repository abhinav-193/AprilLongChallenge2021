def check(pip):
    r=pip%4
    ans=((pip-r)//4)*44
    if r==0:
        return ans+16
    elif r==1:
        return ans+32
    elif r==2:
        return ans+44
    else:
        return ans+55







test=int(input())
for i in range(test):
    pip=int(input())
    dic={1:20, 2:36, 3:51, 4:60}
    if pip<=4:
        print(dic[pip])
    else:
        print(check(pip))
