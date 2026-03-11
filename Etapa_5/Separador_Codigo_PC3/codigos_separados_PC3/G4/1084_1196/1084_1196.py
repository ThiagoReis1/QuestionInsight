A = float(input("nota A: "))
B = float(input("nota B: "))
C = float(input("nota C: "))
D = float(input("nota D: "))
media = (A + B + C + D) / 4
if (media >= 6):
	print(round(media,1))
	print("Aprovado")
else:
	print(round(media,1))
	print("Reprovado")
	