madruga_renda = float(input())
pague_o_aluguel = float(input())

if(pague_o_aluguel > (0.20 * madruga_renda)):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")