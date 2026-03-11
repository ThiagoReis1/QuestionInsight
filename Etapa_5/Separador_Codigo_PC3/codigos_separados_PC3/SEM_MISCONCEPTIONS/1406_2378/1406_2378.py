#Universidade Federal do Amazonas
#Caio Sombra

tipo_de_ataque = input("insira o ataque: ")
n = int(input("digite um num de 1 a 4: "))
turno = int(input("digite quantos turnos: "))

if(tipo_de_ataque == "cauda"):
	dano = n*turno
	
else:
	dano = 2*n*turno
	
print(dano)
	
	
	