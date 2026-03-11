bolo_salgado = input("B ou S: ")
quant_itens = int(input("itens: "))
quant_capp = int(input("Capuccinos: "))

if bolo_salgado == 'B':
	print(quant_itens * 5.00 + quant_capp * 7.50)
else: 
	print(quant_itens * 4.00 + quant_capp * 7.50)