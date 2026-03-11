x = float(input("informe o valor da prova: "))
y = float(input("informe o valor da prova: "))
z = float(input("informe o valor da prova: "))
w = float(input("informe o valor da prova: "))
media = ((x + y + z + w) / 4) 
if(media >= 6):
	print(round(media, 1))
	print("Aprovado")
else:
	print(round(media, 1))
	print("Reprovado")