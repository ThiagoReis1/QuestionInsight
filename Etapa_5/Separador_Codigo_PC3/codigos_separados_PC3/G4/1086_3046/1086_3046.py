n1 = float(input("informe a primeira nota: "))
n2 = float(input("informe a segunda nota: "))
n3 = float(input("informe a terceira nota: "))

ma = (n1+n2+n3) / 3

if(ma >= 7):
	print(round(ma, 1))
	print("Aprovado")
else:
	print(round(ma, 1))
	print("Reprovado")