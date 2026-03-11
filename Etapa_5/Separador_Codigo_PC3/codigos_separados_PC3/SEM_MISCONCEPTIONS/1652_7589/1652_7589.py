from numpy import *

v = input("Coloque a etnia de cada alunos: ").upper().split(',')

quant_B = 0

quant_PA = 0

quant_PR = 0

quant_A = 0

quant_I = 0

i = 0

while(i < len(v)):
	if (v[i] == "B"):
		quant_B = quant_B + 1
	if (v[i] == "PA"):
		quant_PA = quant_PA + 1
	if (v[i] == "PR"):
		quant_PR = quant_PR + 1
	if (v[i] == "A"):
		quant_A = quant_A + 1
	if (v[i] == "I"):
		quant_I = quant_I + 1
	i = i + 1
	
a = array([quant_B, quant_PA, quant_PR, quant_A, quant_I])

print(max(a))

print(a)