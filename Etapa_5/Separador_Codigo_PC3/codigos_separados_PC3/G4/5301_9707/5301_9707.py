v = float(input("v: "))

cont = 0

while (v >= 40):
	cont = cont + 1
	v =  v -v*(2/100) 
	
print(cont)