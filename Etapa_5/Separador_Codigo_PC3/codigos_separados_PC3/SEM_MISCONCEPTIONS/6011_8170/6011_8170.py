ren = float(input("Renda de Carla: "))
prest = float(input("Valor da prestacao: "))

x = ren * (35/100)

if (prest>x):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")