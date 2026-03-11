

x1 = float(input("g: "))



if x1 <= 5000:
	total= (x1 * 0.03) + 20.00
elif x1 > 5001 and x1 < 6000:
	total= (x1 * 0.04)+ 25.00
elif x1 > 6001 and x1 < 7000:
	total = (x1 * 0.05)+ 30.00
elif x1 > 7000:
	total = (x1 * 0.06)+ 35.00
	
	
print(round(total, 2))