p1 = float(input("Digite a nota da primeira prova: "))
p2 = float(input("Digite a nota da segunda prova: "))
p3 = float(input("Digite a nota da terceira prova: "))
p4 = float(input("Digite a nota da quarta prova: "))

ma = (p1+p2+p3+p4)/4
print(round(ma, 2))

if(ma >= 5):
	print("Aprovacao")
else:
	print("Reprovacao")
	

