m = input("O ou K: ")
vm = float(input("valor da medida: "))
if(m == "O"):
	p = (vm / 35.274) 
else:
	p =  (35.274 * vm)
print(round(p, 2))