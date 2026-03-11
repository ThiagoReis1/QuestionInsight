#Entradas
pc = float(input("Insira o preco de custo: "))
#Condições
if(pc > 0):
	if(pc<=50):
		vv = pc + pc*1
		print(round(vv,2))
	elif(50.01 <=  pc <= 100.0):
		vv = pc + pc*0.5
		print(round(vv,2))
	elif(100.1 <= pc <= 500.0):
		vv = pc + pc*0.4
		print(round(vv,2))
	elif(pc > 500):
		vv = pc + pc*0.3
		print(round(vv,2))