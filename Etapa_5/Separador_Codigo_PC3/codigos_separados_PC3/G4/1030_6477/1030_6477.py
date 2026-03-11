from math import*

qm = float(input("Qual a quantidade de minutos excedentes consumidos durante certo mes: "))

b = 0.97* qm
c = b + 45
d = c * 42/100
e = c + d

print(round(e,2))