v = int(input("codigo do cargo:"))
s = float(input("salario do ninja atual:"))

c= s*(10/100)+s
j= s*(30/100)+s

if (v==101):
	msg = c
	print (round(msg,2))
	print ("Aumento de 10 porcento")
	
else :
	msg = j
	print(round(msg,2))
	print("Aumento de 30 porcento")