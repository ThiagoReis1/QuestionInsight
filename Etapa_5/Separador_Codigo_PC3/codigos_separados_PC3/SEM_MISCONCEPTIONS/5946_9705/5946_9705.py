lanche = input("L ou P:")
quant1 = int(input("quant1: "))
quant2 = int(input("quant2: "))

if lanche == "L":
	conta = quant1 * 6.00 + quant2 * 3.00
	
else:
	conta = quant1 * 4.5 + quant2 * 3.00
	
print(conta)