tp = str(input("Informe o item (T ou P): ")).upper()
qtp = int(input("Informe a quantidade: "))
qc = int(input("Informe quantas bebidas: "))

t = 6
p = 5
c = 4.5

if tp == "T":
	conta = t * qtp + c * qc
	print(float(round(conta, 2)))
	
else:
	conta = p * qtp + c * qc
	print(float(round(conta, 2)))