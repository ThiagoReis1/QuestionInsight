tipo_ataque = input()
quantidade_baforada = int(input())
if tipo_ataque == 'maritimo':
	quantidade_unidade = quantidade_baforada*40
	print("Viserion")
	print(quantidade_unidade)
else:
	quantidade_unidade = quantidade_baforada*150
	print("Drogon")
	print(quantidade_unidade)