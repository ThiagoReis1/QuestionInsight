g = int(input("combustivel: "))

if (g > 0) and (g < 17.5):
	total = g + 0.8 
elif (g >= 17.5) and (g < 35.0):
	total = g + 1.3
elif (g >= 35.0) and (g < 50.0):
	total = g + 2.1
else:
	total = g + 3.0
	
total = round(total, 2)
print(total)