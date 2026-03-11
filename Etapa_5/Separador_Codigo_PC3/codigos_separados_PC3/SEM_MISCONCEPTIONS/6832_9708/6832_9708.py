H = 5.40
C = 8.95
L = 4.50
compras = input().upper()

i = 0
total = 0

while i < len(compras):
	if compras[i] == "H":
		total = total + H
	if compras[i] == "C":
		total = total + C
	if compras[i] == "L":
		total = total + L
	i = i+1
print(round(total, 2))