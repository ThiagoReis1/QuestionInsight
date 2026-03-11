cliente= float(input("cliente"))

if(cliente<=150):
	cliente1= float((cliente *0.60) +5.00	)
	print(round(cliente1,2))	
else:
	cliente2= float((cliente *0.75)+16)
	print(round(cliente2,2))