from math import*
nivel = int(input("nivel: "))
horas = float(input("horas: "))
			  
if(nivel == 1):
	s = horas * 12
elif(nivel == 2):
	s = horas * 17
elif(nivel == 3):
	s = horas * 25
else:
	print("invalido")

print(round(s, 2))