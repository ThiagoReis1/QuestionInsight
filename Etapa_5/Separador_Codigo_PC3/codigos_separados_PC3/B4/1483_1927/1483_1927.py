equip = input("")
quant = int(input(""))

comp = 12
freezer = 52
fura = 1.7
liqui = 1.8
micro = 15
notebook = 2.5
tele = 15
venti = 2.4

if(quant<0) or (quant>1000) and (equip!=COMPUTADOR) and (equip!=FREEZER) and (equip!=FURADEIRA) and (equip!=LIQUIDIFICADOR) and (equip!=MICROONDAS) and (equip!=NOTEBOOK) and (equip!=TELEVISOR) and (equip!=VENTILADOR):
	print("Entrada invalida")
else:
	if(equip=='COMPUTADOR'):
		peso_comp = comp*quant
		print(peso_comp)
	else:
		if(equip=='FREEZER'):
			print(freezer*quant)
		else:
			if(equip=='FURADEIRA'):
				print(fura*quant)
			else:
				if(equip=='LIQUIDIFICADOR'):
					print(liqui*quant)
				else:
					if(equip=='MICROONDAS'):
						print(micro*quant)
					else:
						if(equip=='NOTEBOOK'):
							print(notebook*quant)
						else:
							if(equip=='TELEVISOR'):
								print(tele*quant)
							else:
								if(equip=='VENTILADOR'):
									print(venti*quant)
								else:
									print("Entrada invalida")