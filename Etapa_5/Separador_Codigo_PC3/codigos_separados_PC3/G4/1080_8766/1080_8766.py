a = float(input("Digite a nota a:"))
b = float(input("Digite a nota b:"))
c = float(input("Digite a nota c:"))


media = (a + b + c)/3
if media >= 5:
	print(round(media,1))
	print("Aprovado")
else:
	print(round(media,1))
	print("Reprovado")

