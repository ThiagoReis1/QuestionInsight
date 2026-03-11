c = input("lanche ou pizza:")
q = int(input("quantidade de lanches ou pizzas:"))
r = int(input("refrigerantes:"))
l = 6.00
p= 4.50
a= 3.00

	
if c== "L":
	t = l*q+(r*3)
	print(round(t,2))
else: 
	s = (p*q)+(r*3)
	print(round(s,2))
	
