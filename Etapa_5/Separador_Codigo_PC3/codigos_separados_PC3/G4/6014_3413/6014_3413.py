def ag(r,p):
	b = r * 0.35
	if p > b:
		print("Emprestimo nao aprovado")
	else:
		print("Emprestimo aprovado")
	
ag(float(input()), float(input()))