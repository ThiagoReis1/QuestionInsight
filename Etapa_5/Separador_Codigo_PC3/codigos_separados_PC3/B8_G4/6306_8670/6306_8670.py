nome = input("Informe a secao do produto: ").upper()

i = 0
j = 0
k = 0
l = 0
total = 0

while i < len(nome):
	
	if nome[i] == "A":
		total = total + 19.90
		j = j + 1
		
	elif nome[i] == "L":
		total = total + 3.50
		k = k + 1
		
	elif nome[i] == "P":
		total = total + 4.25
		l = l + 1
		
	i = i + 1
	
print(round(total, 2), j, k, l)