
prova1 = float(input("nota da primeira prova: "))
prova2 = float(input("nota da segunda prova: "))
prova3 = float(input("nota da terceira prova: "))
prova4 = float(input("nota da quarta prova: "))

total = (prova1 + prova2 + prova3 + prova4) / 4

if(total >= 5):
	print(round(total, 2))
	print("Aprovacao")
else:
	print(round(total, 2))
	print("Reprovacao")