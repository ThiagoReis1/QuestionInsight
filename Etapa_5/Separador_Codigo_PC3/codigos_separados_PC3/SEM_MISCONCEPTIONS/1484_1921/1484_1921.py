equipamento = input().upper()
capacidade = int(input())
computador = 12
freezer = 52
furadeira = 1.7
liquidificador = 1.8
microondas = 15
notebook = 2.5
televisor = 15
ventilador = 2.4
if(equipamento == "COMPUTADOR"):
	quantidade = capacidade/computador
	if(quantidade < 0 or quantidade > 1000):
		print("Entrada invalida".upper())
	else:
		print(int(quantidade))
elif(equipamento == "FREEZER"):
	quantidade = capacidade/freezer
	if(quantidade < 0 or quantidade > 1000):
		print("Entrada invalida".upper())
	else:
		print(int(quantidade))
	
elif(equipamento == "FURADEIRA"):
	quantidade = capacidade/furadeira
	if(quantidade < 0 or quantidade > 1000):
		print("Entrada invalida".upper())
	else:
		print(int(quantidade))
	
elif(equipamento == "LIQUIDIFICADOR"):
	quantidade = capacidade/liquidificador
	if(quantidade < 0 or quantidade > 1000):
		print("Entrada invalida".upper())
	else:
		print(int(quantidade))
	
elif(equipamento == "MICROONDAS"):
	quantidade = capacidade/microondas
	if(quantidade < 0 or quantidade > 1000):
		print("Entrada invalida".upper())
	else:
		print(int(quantidade))
elif(equipamento == "NOTEBOOK"):
	quantidade = capacidade/notebook
	if(quantidade < 0 or quantidade > 1000):
		print("Entrada invalida".upper())
	else:
		print(int(quantidade))
	
elif(equipamento == "TELEVISOR"):
	quantidade = capacidade/televisor
	if(quantidade < 0 or quantidade > 1000):
		print("Entrada invalida".upper())
	else:
		print(int(quantidade))
elif(equipamento == "VENTILADOR"):
	quantidade = capacidade/ventilador
	if(quantidade < 0 or quantidade > 1000):
		print("Entrada invalida".upper())
	else:
		print(int(quantidade))	

else:
	print("Entrada invalida")