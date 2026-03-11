carne = 19.90
leite = 3.50
pao = 4.25

lista = input().upper()

i = 0
total = 0

while i < len(lista):
	if lista[i] == "A":
		total = total + carne
	elif lista[i] == "L":
		total = total + leite
	elif lista[i] == "P":
		total = total + pao
	i = i + 1
print(round(total,2))

