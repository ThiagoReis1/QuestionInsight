price = float(input("Preco: "))
code = int(input("Codigo: "))

discount = 0.4
avb_code = [1, 2, 3, 4]

if code in avb_code:
	if code == 1:
		f = 0.1
	elif code == 2:
		f = 0.08
	elif code == 3:
		f = 0
	elif code == 4:
		f = 0.02

venda = price * (1 - discount) + (price * f)

print(round(venda,2))
		
