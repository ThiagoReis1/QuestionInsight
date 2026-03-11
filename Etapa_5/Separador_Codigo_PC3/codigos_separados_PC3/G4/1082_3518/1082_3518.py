n1= float(input("valor 1"))
n2= float(input("valor 2"))
n3= float(input("valor 3"))
n4= float(input("valor 4"))
n5= float(input("valor 5"))
media= (n1+n2+n3+n4+n5)/5
print(round(media, 1))
if(media >= 5.0):
	print("Aprovado")
else:
	print("Reprovado")
