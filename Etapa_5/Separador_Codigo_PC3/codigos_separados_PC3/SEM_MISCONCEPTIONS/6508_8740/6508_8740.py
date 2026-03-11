vara = int(input("quantidade de combos: "))
quant = vara*50
if vara <= 4:
	print(quant)
if vara >=5:
	varc = quant*(12/100)
	vartt= quant - varc
	print(vartt)