n1=float(input("Digite a nota 1: "))
n2=float(input("Digite a nota 2: "))
n3=float(input("Digite a nota 3: "))
n4=float(input("Digite a nota 4: "))
n5=float(input("Digite a nota 5: "))

media=(n1+n2+n3+n4+n5)/5
media=round(media,2)

if media>=6:
	print(media)
	print("Aprovado")
else:
	print(media)
	print("Reprovado")