r = float(input("valor da renda da carla: "))
p = float(input("valor da prestacao: "))

if p > (35/100)*r:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")