x = input("digite o aminoacido: ".upper())
O = 15.9994
C = 12.011 
N = 14.00674 
H = 1.0079 
GLICINA = (2*C)+(5*H)+(N)+(2*O)
PROLINA = (5*C)+(10*H)+(N)+(2*O)
SERINA = (3*C)+(7*H)+(N)+(3*O)

if(x == "GLICINA"):
	print(round(GLICINA,2))
elif(x == "PROLINA"):
	print(round(PROLINA,2))
elif(x == "SERINA"):
	print(round(SERINA,2))
else:
	print("Entrada:",)
	print("Dado Invalido")
			