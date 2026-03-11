k= float(input("Frete:"))



if (4999.999 > k    or k == 4999.999 ):
	print(round((k * 0.05), 2))

else: 
	print(round((k * 0.04 + 60.00) , 2  )) 
		