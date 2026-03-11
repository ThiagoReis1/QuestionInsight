ataque = input("Digite o tipo de ataque realizado: ")
N = int(input("Digite o valor sorteadono dado: "))
turnos = int(input("Número de turnos que o personagem fica ferido: "))
#cauda
if(ataque == "cauda"):
	pvp = N * turnos
#cuspe
if(ataque == "cuspe"):
	pvp = (2 * N) * turnos
print(pvp)
