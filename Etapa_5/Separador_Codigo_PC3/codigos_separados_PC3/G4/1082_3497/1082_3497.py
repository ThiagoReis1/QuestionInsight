n1 = float(input("valor nota 1:"))
n2 = float(input("valor nota 2:"))
n3 = float(input("valor nota 3:"))
n4 = float(input("valor nota 4:"))
n5 = float(input("valor nota 5:"))

aritmetica = (n1+n2+n3+n4+n5)/5

if(aritmetica>5):
	print(round(aritmetica, 1))
	print("Aprovado")
	
else:
	print(round(aritmetica, 1))
	print("Reprovado")