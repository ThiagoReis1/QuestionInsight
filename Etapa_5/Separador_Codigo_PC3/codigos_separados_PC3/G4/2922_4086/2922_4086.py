qi=float(input("valor inicial: "))
qf=float(input("valor final: "))
t=(input("meses: "))

i=((qf/qi)**(1/t))-1
print(round(i, 5))