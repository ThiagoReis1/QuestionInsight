o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
glutamina = 5*c+8*h+n+4*o
histidina = 6*c+10*h+3*n+2*o
prolina = 5*c+10*h+n+2*o
nome = input().lower()
if(nome == "glutamina"):
	print(round(glutamina,2))
elif(nome == "histidina"):
	print(round(histidina,2))
elif(nome == "prolina"):
	print(round(prolina,2))
else:
	print("Entrada: ",nome.lower())
	print("Dado Invalido")