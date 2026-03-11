#maca = 0.30 se for <12
#se for >=12 maca = 0.25

macas = int(input("Macas: "))

if macas >=12:
	print(round(macas*0.25,2))
else:
	print(round(macas*0.30,2))