nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))
nota3 = float(input("Terceira nota:"))
nota4 = float(input("Quarta nota:"))
nota5 = float(input("Quinta nota:"))

ma = ( nota1 + nota2 + nota3 + nota4 + nota5) / 5

if (ma >= 7) :
	print(round(ma,2))
	print("Aprovacao")
	
else :
	print(round(ma,2))
	print("Reprovacao")