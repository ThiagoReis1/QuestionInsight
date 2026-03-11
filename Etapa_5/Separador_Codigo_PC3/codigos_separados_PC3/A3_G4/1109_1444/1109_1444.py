#Osenildo Maciel
#Peso
X = int(input("Entre com a idade: "))
Y = float(input("Entre com o peso: "))
print("Entradas: ",X,"anos e",Y,"kg")
if X > 0 or not(Y >= 1000):
	if X >= 12 and Y >= 60:
		d = 1000
	if X >= 12 and  0 <= Y < 60:
		d = 875
	if X < 12 and 0 <= Y <= 5:
		d = 5
	if X < 12 and 5 < Y <= 9:
		d = 125
	if X < 12 and 9 < Y <= 16:
		d = 250
	if X < 12 and 16 < Y <= 24:
		d = 375
	print("Dosagem:",d,"mg")
else:
	print("Dados invalidos")