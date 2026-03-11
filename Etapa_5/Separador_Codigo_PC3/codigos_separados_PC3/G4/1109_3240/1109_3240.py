i = int(input("Digite a idade: "))
p = float(input("Digite o peso: "))
if(i >= 12 and i <=130 and p >= 60 and p <= 550):
	print("Entradas:", i, "anos", "e", p, "kg")
	print("Dosagem: 1000 mg")
elif(i >= 12 and i <=130 and p < 60 and p <= 550):
	print("Entradas:", i, "anos", "e", p, "kg")
	print("Dosagem: 875 mg")
elif(i < 12 and i <=130 and p <= 5 and p <= 550):
	print("Entradas:", i, "anos", "e", p, "kg")
	print("Dosagem: 75 mg")
elif(i < 12 and i <=130 and p > 5 and p <= 9 and p <= 550):
	print("Entradas:", i, "anos", "e", p, "kg")
	print("Dosagem: 125 mg")
elif(i < 12 and i <=130 and p > 9 and p <= 16 and p <= 550):
	print("Entradas:", i, "anos", "e", p, "kg")
	print("Dosagem: 250 mg")
elif(i < 12 and i <=130 and p > 16 and p <= 24 and p <= 550):
	print("Entradas:", i, "anos", "e", p, "kg")
	print("Dosagem: 375 mg")
elif(i < 12 and i <=130 and p > 24 and p <= 30 and p <= 550):
	print("Entradas:", i, "anos", "e", p, "kg")
	print("Dosagem: 500 mg")
elif(i < 12 and i <=130 and p > 30 and p <= 550):
	print("Entradas:", i, "anos", "e", p, "kg")
	print("Dosagem: 750 mg")
else:
	print("Entradas:", i, "anos", "e", p, "kg")
	print("Dados invalidos")