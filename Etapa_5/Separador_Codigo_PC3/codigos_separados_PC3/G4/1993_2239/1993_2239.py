amino = input()
m = amino.lower()
O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794
S = 32.066

if(amino.lower() == "cisteina"):
    cis = (C*3+H*7+N+O*2+S)
    a = round(cis,2)
    print(a)
elif(amino.lower() == "isoleucina"):
    iso = (C*6+H*13+N+O*2)
    b = round(iso,2)
    print(b)
elif(amino.lower() == "metionina"):
    met = (C*5+H*11+N+O*2+S)
    c = round(met,2)
    print(c)
else:
    print("Entrada:",m)
    print("Dado Invalido")