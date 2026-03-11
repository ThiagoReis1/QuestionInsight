nota1 = float(input("Digite a 1 nota:"))
nota2 = float(input("Digite a 2 nota:"))
nota3 = float(input("Digite a 3 nota:"))
nota4 = float(input("Digite a 4 nota:"))
if((nota1 + nota2 + nota3 + nota4)/4 >= 5.0):
	situacao = ("Aprovacao")
else:
	situacao = ("Reprovacao")
print(round((nota1+nota2+nota3+nota4)/4 ,2))
print(situacao)