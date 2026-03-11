av1 = float(input("nota da primeira avaliacao: "))
av2 = float(input("nota da segunda avaliacao: "))
av3 = float(input("nota da terceira avaliacao: "))
av4 = float(input("nota da quarta avaliacao: "))
av5 = float(input("nota da quinta avaliacao: "))

md = (av1 + av2 + av3 + av4 + av5)/5

if (md <= 5.0):
	print(round(md, 1), "Reprovado")
else:
	print(round(md, 1), "Aprovado")