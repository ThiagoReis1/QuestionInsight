U_conversao = input("Digie uma letra:")
v_medida = float(input("Digite um valor:"))

if(U_conversao == "K"):
	Oz = 35.274 * v_medida
	print(round(Oz, 2))
else:
	k= v_medida / 35.274
	print(round(k, 2))
	