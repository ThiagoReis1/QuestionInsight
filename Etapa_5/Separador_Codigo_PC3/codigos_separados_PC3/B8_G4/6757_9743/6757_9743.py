p = int(input("numero da quantidade de pizzas"))

p1 = 5*p+4.50
p2 = 5*p+3.25
p3 = 5*p+3

if p>3:
	print(round(p1,2))
	
elif p == 3:
	print(round(p2,2))
	
elif p<3:
	print(round(p3,2))