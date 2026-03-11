nota1 = float(input("nota1: "))
nota2 = float(input("nota2: "))
nota3 = float(input("nota3: "))
nota4 = float(input("nota4: "))
nota5 = float(input("nota5: "))
resultado = (nota1 + nota2 + nota3 + nota4 + nota5)/5
print(round(resultado, 2))
if(resultado >= 7.0):
	print("Aprovacao")
else:
	print("Reprovacao por nota")