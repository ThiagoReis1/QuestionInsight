p1 = float(input("Digite o valor da primeira nota: "))
p2 = float(input("Digite o valor da segunda nota: "))
p3 = float(input("Digite o valor da terceira nota: "))

Pg = (p1+p2+p3)/3

if(Pg >= 6.0):
	print(round(Pg, 2))
	print("Aprovacao")
	
else:
	print(round(Pg, 2))
	print("Reprovacao")
	