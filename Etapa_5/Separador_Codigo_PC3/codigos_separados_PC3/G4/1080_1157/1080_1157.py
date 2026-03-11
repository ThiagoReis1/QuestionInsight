a = float(input("nota1"))
b = float(input("nota2"))
c = float(input("nota3"))
media = round(((a + b + c)/3),1)
if(media >=5):
	print(media)
	print("Aprovado")
else:
	print(media)
	print("Reprovado")