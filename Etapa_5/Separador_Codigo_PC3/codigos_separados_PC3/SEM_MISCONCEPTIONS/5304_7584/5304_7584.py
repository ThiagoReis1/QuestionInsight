numinic = int(input("Qual o numero inicial de bacterias? "))
horas = int(input("Qual a quantidade de horas total? "))

numbact = numinic
cresce = 0.15
cont = 0

while(cont < horas):
	porhora = int(numbact * cresce)
	numbact = numbact + porhora
	
	cont = cont + 1
	print(numbact)