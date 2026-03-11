n1 = float(input("Nota: "))
n2 = float(input("Nota: "))
n3 = float(input("Nota: "))
n4 = float(input("Nota: "))
media = 7.0
ma = (n1+n2+n3+n4)/ 4
print(round(ma, 2))
if(ma >= media):
	print("Aprovado")
else:
	print("Reprovado")