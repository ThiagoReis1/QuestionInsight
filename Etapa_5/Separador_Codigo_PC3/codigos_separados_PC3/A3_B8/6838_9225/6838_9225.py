from numpy import *
produtos = input("Digite as iniciais dos produtos: ")
doces = 0
salgados = 0
integrais = 0
v1 = 0
total = 0

while v1 < len(produtos):
	if produtos[v1] == "D":
		total = total + 2.25
		
	elif produtos[v1] == "S":
		total = total + 4.00
		
	elif produtos[v1] == "I":
		total = total + 6.90
		
	v1= v1 + 1
print(round(total, 2))