amino = input(": aspartato,fenilalanina ou e firosina")
m = amino.lower()
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079
S=32.066
if(amino.lower() == "aspartato"):
    asp = (C*4+H*6+N+O*4)
    a = round(asp,2)
    print(a)
elif(amino.lower() == "fenilalanina"):
    fenil = (C*9+H*11+O*2+S)
    b = round(fenil,2)
    print(b)
elif(amino.lower() == "tirosina"):
    tiro = (C*9+H*11+N+O*3)
    c = round(tiro,2)
    print(c)
else:
    print("Entrada:",m)
    print("Dado Invalido")