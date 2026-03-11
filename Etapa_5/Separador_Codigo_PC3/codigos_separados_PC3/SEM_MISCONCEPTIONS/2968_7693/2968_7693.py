tipo = str(input("digite o que voce deseja. L para lanche e S para salgado: "))
quant1 = int(input("digite a quantidade de lanches ou salgados: "))
quant2 = int(input("digite a quantidaade de refrigerantes: "))

total_L = quant1*5 + quant2*4
total_S = quant1*3.5+quant2*4

if tipo == "L":
	print(round(total_L,2))
if tipo == "S":
	print(round(total_S,2))