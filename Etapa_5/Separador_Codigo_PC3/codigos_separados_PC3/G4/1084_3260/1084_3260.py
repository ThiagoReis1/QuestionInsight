a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
d = float(input("c= "))

M = (a + b + c + d)/4

if M >= 6.0:
	print(round(M, 1))
	print("Aprovado")
else:
	print(round(M, 1))
	print("Reprovado")