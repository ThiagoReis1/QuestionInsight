nota1 = float(input("nota1:"))
nota2 = float(input("nota2:"))
nota3 = float(input("nota3:"))
nota4 = float(input("nota4:"))

media = (nota1+nota2+nota3+nota4)/4 
print(round(media,2))
if media >= 5.0:
	print("Aprovacao")
else:
	print("Reprovacao")