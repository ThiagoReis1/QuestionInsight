#Lucas Nascimento Estevam da Silva	#Matricula: 21602757
#Trabalho Pratico 2
#Exercicio 1

consumo = float(input("Consumo de agua em metros cubicos:"))
taxa = 30.0
valor = 0.0
if(consumo < 10):
	valor = taxa + (consumo * 3.0)
else:
	valor = taxa + (consumo * 3.5)
print(valor)
	