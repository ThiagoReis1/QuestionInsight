sa=float(input("Salario atual: "))

if(sa>=0 and sa<=1212.00):
	var=round(sa+(sa*0.12),2)
	print(var)
	
elif(sa<=5000.00):
	var=round(sa+(sa*0.08),2)
	print(var)
	
else:
	var=round(sa+(sa*0.03),2)
	print(var)



