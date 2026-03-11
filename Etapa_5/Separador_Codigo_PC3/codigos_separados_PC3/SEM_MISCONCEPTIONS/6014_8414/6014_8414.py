renda = round(float(input(" valor da renda: ")),2)
prestacao = round(float(input(" valor da prestacao que pode pagar: ")), 2)

if prestacao > renda*0.35:
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")