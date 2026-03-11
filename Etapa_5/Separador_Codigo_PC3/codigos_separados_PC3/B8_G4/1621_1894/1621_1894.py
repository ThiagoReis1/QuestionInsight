from numpy import *

nome = array(input("nome dos produtos: "))
qtd = array(eval(input("quantidade do produto: ")))

A = 1.25
F = 2.60
B = 1.80
M = 0.85
F2 = 3.20

i = 0

while(i < qtd[i]):
	if (nome[i] == "ARROZ"):
		total = qtd[i] * A
	elif (qtd[i] == "FEIJAO"):
		total = qtd[i] * F
	elif (qtd[i] == "BIS"):
		total = qtd[i] * B
	elif (qtd[i] == "MIOJO"):
		total = qtd[i] * M
	elif (qtd[i] == "FANTA"):
		total = qtd[i] * F2
	i = i + 1
print(total)
	