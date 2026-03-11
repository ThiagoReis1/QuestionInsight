opcao = input("Digite 'B' para bolo e 'S' para salgado")
qt_opcao = int(input("Digite a quantidade:"))
qt_cap = int(input("Digite a quantidade de cappucinos"))
bolo = 5
salgado = 4
cappuccino = 7.50
if opcao == 'B':
	valor_bolo = bolo * qt_opcao
	valor_cap = cappuccino * qt_cap
	valor_total = valor_bolo + valor_cap
	print(valor_total)
else:
	valor_salgado = salgado * qt_opcao
	valor_cap = cappuccino * qt_cap
	valor_total = valor_salgado + valor_cap
	print(valor_total)
			
	