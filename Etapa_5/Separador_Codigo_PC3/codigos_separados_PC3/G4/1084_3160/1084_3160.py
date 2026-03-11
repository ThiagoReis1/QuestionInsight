n1 = float(input("n1"))
n2 = float(input("n2"))
n3 = float(input("n3"))
n4 = float(input("n4"))
resultado = (n1+n2+n3+n4)/4
print(round(resultado,1))
if(resultado>=6.0):
	print("Aprovado")
else:
	print("Reprovado")