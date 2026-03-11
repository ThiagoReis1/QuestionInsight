v = float(input("velocidade da internet: "))

if (v < 50) :
	total = 60 + 4.50 
	print("total=",round(total, 2))
	
elif (v == 50) :
	total = 60 + 5.50
	print("total=", round(total, 2))
	
else :
	total = 60 + 6.50
	print("total=", round(total, 2))