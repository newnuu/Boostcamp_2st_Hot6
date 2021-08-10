def fare(x):
    if x>1000000:
        return 7*(x-1000000)+5*990000+3*9900+2*100
    elif x>10000:
        return 5*(x-10000)+3*9900+2*100
    elif x>100:
        return 3*(x-100)+2*100
    else:
        return 2*x

def elec(fare):
    if fare>(2*100+3*9900+5*990000):
        return 1000000+(fare-(2*100+3*9900+5*990000))//7
    elif fare > (2*100+3*9900):
        return 10000+(fare-(2*100+3*9900))//5
    elif fare > 2*100:
        return 100+(fare-2*100)//3
    else:
        return fare//2
    
while True:    
    s,d = map(int,input().split())
    if s==0 and d==0:
        break
    s1 = elec(s)
    b = s1//2
    a = s1-b
    dd = abs(fare(b)-fare(a))
    dif = s1-b
    while dd!=d:
        dif = dif//2 if dif//2!=0 else 1
        if dd<d:
            b+=dif
        else:
            b-=dif
        a = s1-b
        dd = abs(fare(b)-fare(a))
    print(min(fare(a),fare(b)))
