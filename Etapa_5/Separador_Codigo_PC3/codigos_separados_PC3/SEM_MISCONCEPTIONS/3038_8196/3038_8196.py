var1 = float(input("leia o valor de x: "))

if(var1 <=-1 or var1 >= 1):
	result = abs(var1)**(1/2)
elif(-1 < var1 < 0 or 0 < var1 < 1):
	result = abs(var1)

else:
	result = 0
	
print(round(result,2))
	
	