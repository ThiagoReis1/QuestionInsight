#Universidade Federal do Amazonas
#Jorge Trajano da Silva Junior - 21553770
#Avaliação 04 - Exercício 04
#05/08/2016
nv = int(input("Informe a quantidade inicial de vírus: "))
nl = int(input("Informe a quantidade inicial de leucócitos: "))
tv = float(input("Informe a taxa de multiplicação diaria do virus: "))
tl = float(input("Informe a taxa de multiplicação diaria dos leucocitos: "))
v = nv
l = nl
i = 0
while(v >= 2*l):
	l = l + (l*tl/100)
	v = v + (v*tv/100)
	i = i + 1
print(i)