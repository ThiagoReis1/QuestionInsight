dias = int(input("Qnts dias:"))

if (dias < 7):
	cal = 100*dias + 15
	print(round(cal,2))
	
elif (dias == 7):
	cal = 100*dias + 12
	print(round(cal,2))
	
else:
	cal = 100*dias + 10
	print(round(cal,2))