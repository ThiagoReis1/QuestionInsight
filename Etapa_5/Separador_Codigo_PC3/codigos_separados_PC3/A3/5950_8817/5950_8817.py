t = input()
c = int(input())
p = int(input())


pastel = p*5
cappuccino = c*4.50
total = pastel + cappuccino
if t.upper() == "P":
	total = (c*5.00) + (p*4.50)
	print(round(total,2))
else:
	total = (c*6.00) + (p*4.50)
	print(round(total,2))
	
	