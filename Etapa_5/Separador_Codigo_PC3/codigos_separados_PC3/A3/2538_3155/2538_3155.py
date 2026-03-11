valor_sitio = float(input("Valor Inicial: "))
valor_depositado = float(input("Valor Depositado: "))
valor_mensal = float(input("Valor mensal fixo:"))
tx = float(input("Taxa de Juros: "))
mes = 0
cont = 0
if(valor_sitio > 0 and valor_depositado > 0 and valor_mensal > 0 and tx > 0):
	while(valor_depositado < valor_sitio):
		valor_depositado = valor_depositado + (valor_depositado * (tx / 100)) + valor_mensal
		valor_depositado = round(valor_depositado,2) 
		mes += 1
	print(mes)	
else:
	print("Dados incorretos")
	
