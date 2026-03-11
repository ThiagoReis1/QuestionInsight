c = float(input("consumo em minutos"))
f = 23.00
ic = 31/100
m = 0.28
valor = (f + (c*m))+ic*(f +(c*m))
print(round(valor,2))  