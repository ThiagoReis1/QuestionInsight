v1 = input("Quantos produtos de cada secao levou? (A)cougue, (L)acticinios (P)adaria ou (S) para sair. Por favor marque com as letras correspondentes.").upper()

a = 0
l = 0
p = 0
i = 0
t = len(v1) - 1

while i <= t:
	if v1[i] == "A":
		a += 1
	elif v1[i] == "L":
		l += 1
	elif v1[i] == "P":
		p += 1
	i += 1
total = a * 19.90 + l * 3.50 + p * 4.25
print(round(total,2))