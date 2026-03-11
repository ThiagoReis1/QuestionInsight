quantd = int(input("pizzas : "))
total = 0
if quantd < 3 :
	total = quantd*5 + 3
elif quantd == 3 :
	total = quantd*5 + 3.25
else :
	total = quantd*5 + 4.5
	
print(round(total, 2))