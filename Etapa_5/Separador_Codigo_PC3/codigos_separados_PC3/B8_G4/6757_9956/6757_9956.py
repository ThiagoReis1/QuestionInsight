nump = int(input("numero de pizzas"))


if nump < 3 :
	taxa = 3
	cal= 5*nump + taxa
	print (round(cal,2))
	
elif nump  == 3:
	taxa = 3.25
	cal= 5*nump + taxa
	print(round(cal,2))
	
elif nump > 3 :
	taxa = 4.50
	cal= 5*nump + taxa
	print (round(cal,2))
