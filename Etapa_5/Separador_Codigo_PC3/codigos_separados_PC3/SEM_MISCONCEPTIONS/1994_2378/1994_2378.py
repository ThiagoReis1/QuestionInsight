aminoacido = input("insira nome do aminoacido: ").lower()

o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079

if(aminoacido == "histidina"):
	histidina = (c*6) + (h*10) + (n*3) + (o*2)
	print(round(histidina, 2))
elif(aminoacido == "leucina"):
	leucina = (c*6) + (h*13) + n + (o*2)
	print(round(leucina, 2))
elif(aminoacido == "lisina"):
	lisina = (c*6) + (h*15) + (n*2) + (o*2)
	print(round(lisina, 2))
else:
	print("Entrada: ", aminoacido)
	print("Dado Invalido")