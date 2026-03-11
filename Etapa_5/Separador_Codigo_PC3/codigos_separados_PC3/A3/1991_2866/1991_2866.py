n = (input("aminoacido: "))
#pesos moleculares
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

Glicina = 2*12.011+5*1.0079+14.00674+2*15.9994
Prolina = 5*12.011+10*1.0079+14.00674+2*15.9994
Serina = 3*12.011+7*1.0079+14.00674+3*15.9994
x= Glicina
if(n==Prolina or n==Serina):
	print("Entrada: X")
	print("Dado invalido")
	
else:
	print(round(x,2))