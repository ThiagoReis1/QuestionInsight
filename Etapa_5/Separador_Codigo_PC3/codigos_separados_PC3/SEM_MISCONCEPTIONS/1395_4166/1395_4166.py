valorvendas=float(input("valor de vendas"))
comissao=float(valorvendas*(5/100))
comissao2=float((5/100)*1000+(10/100)*(valorvendas-1000))

if(valorvendas<=1000.00):
	mensagem=comissao
else:
	mensagem=comissao2
	
print(round(mensagem, 2))