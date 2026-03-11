#Dina Karen Barros Vieira
#Trabalho Prático 2
#Exercício 2

#entrada de dados
nom_arm = input("Nome da arma: \"machado\" ou \"lanca\": ")
fator = int(input("Fator de sucesso de 1 a 10:"))

#codificando

if ( nom_arm == "machado" ):
	dano = 30 * (fator/10)
if ( nom_arm == "lanca"):
	dano = 5 + (20 * fator/10)
	
#saida de dados
print (dano)
