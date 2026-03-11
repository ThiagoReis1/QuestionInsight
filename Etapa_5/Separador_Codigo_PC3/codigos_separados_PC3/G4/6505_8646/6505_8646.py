# faça seu código aqui!

t = input("Tipo de combo: ")
tt = t.upper()
q = int(input("Quantidade: "))

if tt == "C":
	op_1 = 30*q
	op_2 = op_1*0.15
	op_3 = op_1 - op_2
	print(op_3)
	
	
else:
	op = 30*q
	print(op)