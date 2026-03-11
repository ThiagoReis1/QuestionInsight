carga = int(input("Carga Horaria: "))

if carga >= 0:
	if carga >= 0 and carga <= 10:
		x = ((carga*50.00)+500.00)
		print(round(x, 2))
	if carga > 10 and carga <= 20:
		x = ((carga*60.00)+600.00)
		print(round(x, 2))
	if carga > 20 and carga <= 30:
		x = ((carga*70.00)+700.00)
		print(round(x, 2))
	if carga > 30:
		x = ((carga*80.00)+800.00)
		print(round(x, 2))