#Lucas Nascimento Estevam da Silva	#Matricula: 21602757
#Trabalho Pratico 2
#Exercicio 3

F = float(input("Pontos de forca iniciais:"))
lua = int(input("Porcentagem de lua visivel:"))
f = F - 23 * (1 - (lua / 100))
if(f < 0):
	print("ATACO")
else:
	print("CORRO")
