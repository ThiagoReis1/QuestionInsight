#Lucas Nascimento Estevam da Silva	Matricula: 21602757
#Trabalho Pratico 03		
#Exercicio 2

consumo = float(input("Consumo de agua:"))

if(consumo >= 0):
	if(0 <= consumo <= 10):
		valor = consumo * 3 + 15
	
	elif(10 < consumo <= 15):
		valor = consumo * 3.5 + 20
	
	elif(15 < consumo <= 20):
		valor = consumo * 4 + 25
	
	elif(consumo > 20):
		valor = consumo * 4.5 + 30

print(round(valor,2))
