ARMA = input("ARMA:")
D = int(input("destreza:"))
vD1 = int(input("valor 1:"))
vD2 = int(input("valor 2:"))

if((vD1<0) or (vD1>10) or (vD2<0) or (vD2>10) or (D<0) ):
	print("Entrada invalida")
elif( ARMA == "CIMITARRA"):
		S = vD1 + vD2
		DANO = 2*S + 2*D
		print(DANO)
elif( ARMA == "KATANA"):
		S = vD1 + vD2
		DANO = 2*S + 2*D
		print(DANO)
elif( ARMA == "SABRE"):
		S = vD1 + vD2
		DANO = S + 2*D
		print(DANO)
else:
	print("Entrada invaida")

	