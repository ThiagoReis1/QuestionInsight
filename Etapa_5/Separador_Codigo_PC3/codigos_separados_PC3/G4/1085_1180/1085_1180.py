n1 = float(input("Informe n1: "))
n2 = float(input("Informe n2: "))
n3 = float(input("informe n3: "))
n4 = float(input("informe n4: "))
n5 = float(input("informe n5: "))
media = (n1 + n2 + n3 + n4 + n5) / 5
print(round(media,2))
if(media >= 6.0):
	print("Aprovado")
else:
	print("Reprovado")