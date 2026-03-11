dias= int (input ("Digite a quantidade de dias reservados: "))

diaria= 175.00

if (dias < 15):
	taxa= 20.00
	total= ( diaria * dias ) + taxa
	print (round (total, 2))
elif (dias == 15):
	taxa= 16.00
	total= (diaria * dias) + taxa 
	print (round (total, 2))
elif (dias > 15):
	taxa= 10.00
	total= (diaria * dias ) + taxa
	print (round ( total, 2))