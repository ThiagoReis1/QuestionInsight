from numpy import*

p = input("Digite:").upper()

vogal = 45.15
caractere = 50.17
i = 0
custo = 0

while i < len(p):
	if p[i] == "A" or p[i]== "E" or p[i]== "I" or p[i] == "O" or p[i]== "U":
		custo = custo + vogal
	else:
		custo = custo + caractere
		
	i = i + 1
		
print(round(custo, 2))