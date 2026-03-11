from math import *
popin = int(input("Populacao inicial de tracajas: "))
taxaanual = float(input("Taxa anual de crescimento: "))
roubo2 = int(input("Número de tracajas roubados: "))

roubo = roubo2 
ano = 0
x = 0
y = 0
while (popin > roubo):
	popin = popin - roubo
	ano = ano+1
	x = popin * taxaanual
	popin = popin + x

print(ano)
	
	


