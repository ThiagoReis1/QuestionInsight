produto = input().upper()
B = 3.75
C = 7.90
E = 9.85
soma = 0
i = 0
while i < len(produto) :
	if produto[i] == "B":
		soma = soma + B
	elif produto[i] == "C":
		soma = soma + C
	elif produto[i] == "E":
		soma = soma + E
	i = i + 1	
print(round(soma,2))
	



