#entradas
bact = int(input("insira o numero de bacterias: "))
taxa = float(input("insira a taxa de crescimento: "))

horas = 0             #qtd de horas transcorridas
dobro = (bact * 2)    #qtd desejada 
new = bact            #acumuladora para o crescimento da colonia

while new <= dobro:
	new = new + (new * taxa/100)
	horas = horas + 1
print(horas)