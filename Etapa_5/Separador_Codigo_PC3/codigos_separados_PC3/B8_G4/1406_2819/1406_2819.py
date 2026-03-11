tipo = input("") #cauda ou cuspe
n = int(input("")) #valor sorteado pelo dado
turnos = int(input("")) #numero de turnos 
if(tipo == "cauda"):
	pvp = n*turnos #pontos de vida perdidos
elif(tipo == "cuspe"):
	pvp = 2*n*turnos
print(pvp)