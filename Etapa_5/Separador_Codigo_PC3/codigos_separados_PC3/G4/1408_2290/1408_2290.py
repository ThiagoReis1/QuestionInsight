arma= input("Digite a arma:  ")
D= input(int())
D1= input(int())
D2= input(int())
S= float(D1 + D2)

dano_katana= int((2 * S) + D)
dano_sabre= int(S + (2 * D))

if (arma == "katana") :
	print(dano_katana)
else:
	print(dano_sabre)