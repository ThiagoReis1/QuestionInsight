n1 = float(input("Primeira Nota:"))
n2 = float(input("Segunda Nota:"))
n3 = float(input("Terceira Nota:"))
n4 = float(input("Quarta Nota:"))
n5 = float(input("Quinta Nota:"))
md = (n1+n2+n3+n4+n5)/5
if (md >= 6):
	print(round(md,2))
	print('Aprovacao')
else:
	print(round(md,2))	
	print("Reprovacao")
