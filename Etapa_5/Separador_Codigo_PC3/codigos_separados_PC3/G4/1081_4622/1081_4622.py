p1 = float(input("digite nota1: "))
p2 = float(input("digite nota2: "))
p3 = float(input("digite nota3: "))
p4 = float(input("digite nota4: "))

ma = (p1 + p2 + p3 +p4) / 4

if( ma >= 5):
	msg = "Aprovacao"
	print(round(ma,2))
	print(msg)
else:
	msg = "Reprovacao"
	print(round(ma,2))
	print(msg)