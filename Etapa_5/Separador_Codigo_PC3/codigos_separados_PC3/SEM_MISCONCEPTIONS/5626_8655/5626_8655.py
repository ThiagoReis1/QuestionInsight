
valorrenda =  float(input("valor da renda"))
valorprestacao = float(input("prestacao"))

if valorprestacao > (0.25 * valorrenda):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")