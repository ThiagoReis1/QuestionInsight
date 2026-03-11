valor_sitio = float(input("Valor Inicial: "))
valor_mensal = float(input("Valor mensal fixo:"))
tx = float(input("Taxa de Juros: "))
poupanca = 0
mes = 0
cont = 0
if(valor_sitio > 0  and valor_mensal > 0 and tx > 0):
	while(poupanca   < valor_sitio * (0.2 * valor_sitio)):
		poupanca = poupanca + (poupanca * (tx / 100)) + valor_mensal
		poupanca = round(poupanca,2) 
		mes += 1
	print(mes)	
else:
	print("Dados incorretos")
	
