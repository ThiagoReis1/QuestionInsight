plate = int(input("Prato: "))
dessert = int(input("Sobremesa: "))
drink = int(input("Bebida: "))

avb_number = [1, 2, 3, 4]

cal_plate = [180, 230, 250, 350]
cal_dessert = [75, 110, 170, 200]
cal_drink = [20, 70, 100, 65]

tcal = 0

if plate and dessert and drink in avb_number:
	tcal = cal_plate[plate-1] + cal_dessert[dessert-1] + cal_drink[drink-1]
	print("Calorias:", tcal, "cal")
else:
	print("Dados invalidos")
