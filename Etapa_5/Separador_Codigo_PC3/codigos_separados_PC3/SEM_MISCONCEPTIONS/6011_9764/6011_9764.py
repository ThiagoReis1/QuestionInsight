renda = float(input("digite um numero: "))
prestacao = float(input("digite um numero: "))
soma = renda * 0.35
if prestacao > soma:
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")