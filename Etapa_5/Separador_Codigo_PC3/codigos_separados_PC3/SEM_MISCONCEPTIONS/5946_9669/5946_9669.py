L_P = input("Entre com L para lanche e P para pizza: ").upper()
qnt_L_ou_P = int(input("quantidade de lanche ou pizza: "))
qnt_refri = int(input("quantidade de refri: "))

valor_t1 = (6 * qnt_L_ou_P) + (3 * qnt_refri)
valor_t2 = (4.50 * qnt_L_ou_P) + (3 * qnt_refri)

if L_P == "L":
	print(round(valor_t1,2))
	
else:
	print(round(valor_t2,2))