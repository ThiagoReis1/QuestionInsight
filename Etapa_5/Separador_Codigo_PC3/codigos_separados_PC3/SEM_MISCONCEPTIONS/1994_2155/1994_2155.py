molecula = input("nome da molecula: ").lower()
o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079
if(molecula == "histidina"):
	histidina = (c*6)+(h*10)+(n*3)+(o*2)
	print(round(histidina, 2))
elif(molecula == "leucina"):
	leucina = (c*6)+(h*13)+n+(o*2)
	print(round(leucina, 2))
elif(molecula == "lisina"):
	lisina = (c*6)+(h*15)+(n*2)+(o*2)
	print(round(lisina, 2))
else:
	print("Entrada:", molecula)
	print("Dado Invalido")
		
	
