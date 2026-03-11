pc = float(input("Preco de custo de uma mercadoria: "))

if(pc <= 50.00):
	p = (100/100) * pc
	vf = pc + p
	print(round(vf, 2))
elif(pc >= 50.00)and(pc <= 100.00):
	p = (50/100) * pc
	vf = pc + p
	print(round(vf, 2))
elif(pc >= 100.00)and(pc <= 500.00):
	p = (40/100) * pc
	vf = pc + p
	print(round(vf, 2))
elif(pc >= 500.00):
	p = (30/100) * pc
	vf = pc + p
	print(round(vf, 2))
