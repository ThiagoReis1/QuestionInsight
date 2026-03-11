from numpy import *
tempo = array(eval(input("tempo de banho: ")))
percentual = array(eval(input("percentual de abertura da torneira: ")))
tam = size(tempo)
cont = 0
l=0
tot=0
while cont<tam:
	l = l + 5 * tempo[cont]*percentual[cont]/100
	cont = cont + 1
fin =  round(l,2)
print(fin)








