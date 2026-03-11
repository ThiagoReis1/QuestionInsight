n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
media = round((n1 + n2 + n3)/3, 1)
print(media)

if(media >= 5.0):
	print("Aprovado")

else: 
	print("Reprovado")