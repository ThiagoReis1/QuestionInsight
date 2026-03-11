
n1 = float(input("nota 1: "))
n2 = float(input("nota 2:"))
n3 = float(input("nota 3:"))

media = (round(float((n1 + n2 + n3)/3),1))
print(media)
if(int(media >= 7)):
	print("Aprovado")
else:
	print("Reprovado")



