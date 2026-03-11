from numpy import *

tempo = array(eval(input("Digite o tempo de banho: ")))
modo = array(eval(input("Digite o modo do banho: ")))

soma = 0
cont = 0

while(cont < size(tempo)):
	if(modo[cont] == "FRIO"):
		soma = soma + 0.005*0*tempo[cont]
	if(modo[cont] == "QUENTE"):
		soma = soma + 0.005*90*tempo[cont]
	if(modo[cont] == "MORNO"):
		soma = soma + 0.005*45*tempo[cont]
	cont = cont + 1
print(round(soma,2))
		#a = 14*0.005*45
#b = 21*0.005*90
#c = 5*0.005*0
#d = 30 *0.005*90
#print(a+b+c+d)