x = input("nome do aminoacido:" ).lower()

histidina = (6*12.011 + 10*1.0079 + 3*14.00674 + 2*15.9994)
leucina = 6*12.011 + 13*1.0079 + 14.00674 + 2*15.9994
lisina = 6*12.011 + 15*1.0079 + 2*14.00674 + 2*15.9994

if(x!= "histidina" and x!= "leucina" and x!="lisina"):
	print("Entrada:",x)
	print("Dado Invalido")
elif(x == "histidina"):
	print(round(histidina,2))
elif(x == "leucina"):
	print(round(leucina,2))
else:
	print(round(lisina,2))
	
