from numpy import *

produtos = input("informe a inicial das secoes onde deseja comprar: ")
adega = 16.75
laticinios = 4.60
padaria = 2.85
total = 0
i = 0

while i < len(produtos):
	produto = produtos[i]
	if produto == 'A':
		total = total + adega
	elif produto == 'L':
		total = total + laticinios
	elif produto == 'P':
		total = total + padaria
		
	i += 1
	
print(round(total, 2))
	