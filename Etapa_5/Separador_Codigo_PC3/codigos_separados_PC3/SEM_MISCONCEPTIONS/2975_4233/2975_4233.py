quant = int(input("Quantidade de sucos: "))
quant_sal = int(input("Quantidade de salgados: "))
valor = float(input("Valor disponivel: "))

total = (quant*3) + (quant_sal*3.5)

if(valor >= total):
   print(round(total,2), "Sim")
else:
	print("Nao")