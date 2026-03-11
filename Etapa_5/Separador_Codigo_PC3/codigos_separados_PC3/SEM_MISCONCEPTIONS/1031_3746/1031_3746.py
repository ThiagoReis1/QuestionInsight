def preco_gasolina(litros):
	servico = 2.86 * litros + 50
	return servico + servico * 34/100
	
	
if __name__ == '__main__':
	litros = float(input("Digite a quantia de gasolina: "))
	print(round(preco_gasolina(litros),2))
	