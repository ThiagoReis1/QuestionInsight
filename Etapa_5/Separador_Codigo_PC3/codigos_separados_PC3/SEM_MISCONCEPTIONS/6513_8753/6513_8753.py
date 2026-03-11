# faça seu código aqui!
quantidade = int(input("quantidade: "))
manha = 20 * quantidade
if quantidade >= 4:
	print(round(manha - (manha * 0.15), 2))
else :
	print(manha)