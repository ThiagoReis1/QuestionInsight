vl1 = float(input("valor da renda da maria: "))
vl2 = float(input("valor da prestacao: "))

renda = vl1 * 0.35

if vl2 <= renda:
	print("Emprestimo aprovado")
	
else: 
	print("Emprestimo nao aprovado")