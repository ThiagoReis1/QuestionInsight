v = float(input("Insira o valor da compra: "))
c = input("insira o codigo da compra: (D/P/C) ")

if c == "D":
	total = v - (12/100) * v
elif c == "P":
	total = v - (12/100) * v
if c == "C":
	n = int(input("em quantas vezes quer pagar?: "))
	if n == 1:
		total = v
	else:
		total = v + (7/100) * v
		
print(round(total, 2))
		
	
	
	
	