#Lucas Nascimento EStevam da Silva		Matricula: 21602757
#Trabalho Pratico 04
#Exercicio 1

cap = 50000
a = int(input("Quantidade inicial de guerreiros na infantaria: "))
b = int(input("Quantidade inicial de guerreiros na cavalaria: "))
c = float(input("Percentual de crescimento da infantaria: "))
d = float(input("Percentual de crescimento da cavalaria: "))
perc_c = c / 100
perc_d = d / 100
mes = 0

if(a > 0 and b > 0):
	
	while(a + b < cap):
		a = a + a * perc_c
		b = b + b * perc_d
		mes = mes + 1
	
print(mes)