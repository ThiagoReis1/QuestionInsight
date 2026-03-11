hrs = float(input("horas:")) 
hrs_extra = hrs - 20

hrs_1 = hrs - hrs_extra


if  (hrs <= 20 ):
	print(round(hrs*50 , 2))
	
else:
	print(round(hrs_1*50 + hrs_extra*70, 2))	

