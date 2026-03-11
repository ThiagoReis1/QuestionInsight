#Dina Karen Barros Vieira
#Trabalho Prático 2
#Exercício 1

#entrada de dados
temp = float(input("Tempo de voo:"))

#codificando
if (temp <= 200):
	custo = 5000 + temp * 100
else:
	custo = 8000 + (200*100) + ( (temp - 200) * 90)
	
print (round(custo, 2))