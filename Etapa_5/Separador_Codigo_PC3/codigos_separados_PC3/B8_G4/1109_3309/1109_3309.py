x = int(input("insira idade: "))
y = float(input("insira peso: "))

if (x >= 12) and (x < 130) and (y >= 60) and (y < 550.0):
	print("Entradas: ", x, "anos", "e", y, "kg")
	print("Dosagem: 1000 mg")
elif (x >= 12) and (y < 60):
	print("Entradas: ", x, "anos", "e", y, "kg")
	print("Dosagem: 875 mg")

if (x < 12) and (y <= 5):
	print("Entradas: ", x, "anos", "e", y, "kg")
	print("Dosagem: 75 mg")
elif (x < 12) and (y > 5) and (y <= 9):
	print("Entradas: ", x, "anos", "e", y, "kg")
	print("Dosagem: 125 mg")
elif (x < 12) and (y > 9) and (y <= 16):
	print("Entradas: ", x, "anos", "e", y, "kg")
	print("Dosagem: 250 mg")
elif (x < 12) and (y > 16) and (y <= 24):
	print("Entradas: ", x, "anos", "e", y, "kg")
	print("Dosagem: 375 mg")
elif (x < 12) and (y > 24) and (y <= 30):
	print("Entradas: ", x, "anos", "e", y, "kg")
	print("Dosagem: 500 mg")
elif (x < 12) and (y > 30):
	print("Entradas: ", x, "anos", "e", y, "kg")
	print("Dosagem: 750 mg")
	
if (0 < x < 130) and (0.0 < y < 550.0):
	print()
else:
	print("Dados invalidos")