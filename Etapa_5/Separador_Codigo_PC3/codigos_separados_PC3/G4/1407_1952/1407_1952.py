#Lucas Nascimento Estevam da Silva	#Matricula: 21602757
#Trabalho Pratico 2
#Exercicio 2

a = int(input("Quantidade inicial de pontos de vida:"))
b = int(input("Primeiro valor sorteado:"))
c = int(input("Segundo valor sorteado:"))
d = int(input("Terceiro valor sorteado:"))


if((1 <= b <= 12) and (1 <= c <= 12) and (1 <= d <= 12)):
	N = (b + c + d)
	Dano = 10 * N
	Resto = a - Dano	
	if(Resto > 0):
		print("VIVO")
	else:
		print("0")
		print("MORTO") 

	