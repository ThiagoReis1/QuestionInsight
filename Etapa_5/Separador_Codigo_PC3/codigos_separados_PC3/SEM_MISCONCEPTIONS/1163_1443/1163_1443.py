#Igor R Chicolet da Silva
#No de Matricula: 21204615
#Avaliacao Parcial 04

l = int(input("Qual a populacao inicial de lambaris? "))
t = int(input("Qual a populacao inicial de tucunares? "))
taxa_l = float(input("Qual a taxa mensal de crescimento dos lambaris: "))
taxa_t = float(input("Qual a taxa mensal de crescimento dos tucunares: "))

tempo = 0 #em meses

while(l >= t):
	l = l * (1 + taxa_l) ** (tempo + 1)	
	l = l - 2 * t
	
	t = t * (1 + taxa_t) ** (tempo + 1)
	
	tempo = tempo + 1
	
print(tempo)
	
	