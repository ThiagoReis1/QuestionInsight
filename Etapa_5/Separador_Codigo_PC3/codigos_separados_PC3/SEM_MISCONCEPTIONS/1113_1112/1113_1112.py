a=int(input("Qual e a sua idade:"))
b=float(input("Qual e o seu peso:"))
if(a > 130 and  0 < b or  b > 550.0):
	c ="Dados invalidos"
elif(a<=20 and b<=60):
	c= 9
elif(a<=20 and  60 > b <= 90):
	c= 8
elif(a<=20 and  b > 90):
	c= 7
elif(20 < a or a >=50 and b<=60):
	c= 6
elif(20 < a or a >=50 and 60 > b <= 90):
	c= 5
elif(20 < a or a >=50 and b > 90):
	c= 4
elif(50 > a >=130 and b<=60):
	c= 3
elif(50 > a >=130 and 60 > b <= 90):
	c= 2
elif(0 < a >=130 and  90 > b <=550):
	c= 1
print("Entradas:" , a, "anos e" , b, "Kg")
	if (c ="Dados invalidos"):
	print("Dados invalidos")
	else:
	print("Grupo de risco:" ,c)	