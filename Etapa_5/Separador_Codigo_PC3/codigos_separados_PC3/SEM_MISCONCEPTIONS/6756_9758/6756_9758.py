reserva = int(input("reserva de dias: "))
x = 175*reserva
if reserva < 15:
	taxa = 20 
elif reserva == 15:
	taxa = 16 
else:
	taxa = 10 
	
print(float(round(x+taxa, 2)))
	
