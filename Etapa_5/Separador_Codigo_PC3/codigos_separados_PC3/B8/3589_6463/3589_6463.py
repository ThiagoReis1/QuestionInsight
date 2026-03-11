from numpy import * 

pontos = array(eval(input("qual a pontuacao: ")))

i = 0
cont = 0

while (i< cont):
	i = i + 1
	cont= cont + pontos
	if pontos == "1":
		cont= cont * 80
	elif pontos == "2":
		cont = cont * 40
	elif pontos == "3":
		cont = cont * 20
	elif pontos == "4":
		cont = cont * 10
print(sum(cont))
