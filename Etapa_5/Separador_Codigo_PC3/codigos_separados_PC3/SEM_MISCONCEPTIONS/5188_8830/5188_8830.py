vrenda = float(input("Quanto Dona Florinda ganha?: "))
vprestacao = float(input("Quanto ela pode pagar no aluguel mensal?: "))

if (vprestacao/vrenda)>(25/100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")