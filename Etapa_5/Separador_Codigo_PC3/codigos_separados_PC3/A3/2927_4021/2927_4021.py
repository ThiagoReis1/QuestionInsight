#bebidas
suco=3.00
refrigerante=3.50
#salgados
esfirra=1.50

vb=float(input("qual o valor de sua bebida?"))
qe=int(input("qual a quantidade de esfirras?"))

total=vb+qe*esfirra

print(round(total,2))