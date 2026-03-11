nome = input("Informe o aminoacido: ")
C = 12.011
O = 15.9994
N = 14.00674
H = 1.0079
Histidina = C*6 + H*10 + N*3 + O*2
Leucina = C*6 + H*13 + N + O*2
Lisina = C*6 + H*15 + N*2 + O*2
if(nome=="Histidina"):
	print(round(Histidina, 2))
elif(nome=="Leucina"):
	print(round(Leucina, 2))
elif(nome=="Lisina"):
	print(round(Lisina, 2))
else:
	print(nome.lower())

	
			