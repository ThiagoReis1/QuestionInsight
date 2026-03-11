n1 = float(input("digite"))
n2 = float(input("digite"))
n3 = float(input("digite"))
n4 = float(input("digite"))
media = (n1 + n2 + n3 + n4)/4

if(media >= 6.0):
	print(round(media,1))
	print("Aprovado")
	
else:
	print(round(media,1))
	print("Reprovado")