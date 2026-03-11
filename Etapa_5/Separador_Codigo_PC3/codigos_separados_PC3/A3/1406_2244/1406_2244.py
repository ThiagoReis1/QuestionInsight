ataque= input("Informe o tipo de ataque:")
N= int(input("Informe o valor sorteado:"))
turnos= int(input("Informe o numero de turnos:"))
#cauda
if(ataque == "cauda"):
	pvp= N* turnos
#cuspe
if(ataque == "cuspe"):
	pvp= (2*N) * turnos
print(pvp)