from numpy import *

saques = [2100,500,120,2000,2200]
cont = 0


for i in saques: 
	if (i >= 2000):
		cont = cont + 1
print(cont)

d = 0
quant = []

for j in range(size(saques)):
	if (saques[j] >= 2000):
		quant = j
	
print(quant)