tipo = input("Digite uma letra:")
q_ls = int(input("Digite um valor:"))
q_ref = int(input("Digite um valor:"))
if (tipo == "L"):
	p_final = q_ls * 5.00 + q_ref * 4.00
	print(p_final)
else:
	p_final = q_ls * 3.50 + q_ref * 4.00
	print(p_final)