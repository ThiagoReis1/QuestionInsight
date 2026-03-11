cons = float(input("consumo de energia: "))

if(cons < 100):
	total = cons*0.5 + 50
	print(round(total, 2))
else:
	if(100<=cons<250):
		total = cons*0.75 + 50
		print(round(total, 2))
	else:
		if(250<=cons<500):
			total = cons*1 + 50
			print(round(total,2))
		else:
			total = cons*1.25 + 50
			print(round(total, 2))
	
