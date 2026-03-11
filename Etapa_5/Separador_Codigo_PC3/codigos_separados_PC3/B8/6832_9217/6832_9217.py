from numpy import *
produtos = input("digite as iniciais dos produtos: ").upper()
i = 0
total = 0

while i < len(produtos):
	if produtos[i] == "H":
		total = total + 5.4
		
	elif produtos[i] == "C":
		total = total + 8.95
		
	elif produtos[i] == "L":
		total = total + 4.5
	i = i + 1
print(round(total, 2))