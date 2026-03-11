valorrenda = float(input("Informe o valor da renda de dona Cleide: "))
valorprestacao =  float(input("Informe o valor da prestacao de dona Cleide: "))

if valorprestacao >= 0.25 * valorrenda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")