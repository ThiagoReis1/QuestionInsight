from math import*
arv = float(input("arvores: "))
a = float(input("lado do pentagono: "))
pent = ((a**2)*(sqrt(25+10*(sqrt(5)))))/4
quantidade = int(pent*arv)
print(round(quantidade , 2))


