renda = float(input("informe o valor da renda da dona clotilde"))
prestacao = float(input("informe o valor da prestacao que ela pode pagar por mes"))

if prestacao > (0.25*renda):
	print("Emprestimo nao aprovado")

else:
	print("Emprestimo aprovado")