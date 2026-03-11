from math import *
molecula = input("Digite a molecula: ")

PCisteina = (12.011 * 3) + (1.00794*7) + (14.0067*1) + (15.9994*2) + (32.066*1)
PIsoleucina = (12.011*6) + (1.00794*13) + (14.0067*1) + (15.9994*2)
PMetionina  = (12.011*5) + (1.00794*11) + (14.0067*1) + (15.9994*2) + (32.066*1)

if(molecula.lower() == "cisteina"):
	print(round(PCisteina,2))
elif(molecula.lower() == "isoleucina"):
	print(round(PIsoleucina,2))
elif(molecula.lower() == "metionina"):
	print(round(PMetionina,2))
else:
	print("Entrada: ", molecula)
	print("Dado Invalido")
	
