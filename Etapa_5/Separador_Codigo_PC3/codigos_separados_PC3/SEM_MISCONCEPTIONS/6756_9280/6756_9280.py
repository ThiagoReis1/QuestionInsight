dias_reservados = int(input("digite a quantidade de dias reservados: "))
if dias_reservados < 15 :
	taxa_adicional = 20.00
elif dias_reservados == 15.00:
	taxa_adicional = 16.00
else:
	taxa_adicional = 10.00
val_total = 175.00 * dias_reservados + taxa_adicional
print(round(val_total, 2))