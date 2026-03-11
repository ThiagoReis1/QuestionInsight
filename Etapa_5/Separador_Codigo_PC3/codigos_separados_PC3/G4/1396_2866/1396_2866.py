v = float(input("qual valor consumido: "))

#se for consumido 

g = (v / 100 * 10)
e = (v / 100 * 6)

if (v <= 300.0): 
	print(round(v+g, 2))
	
else:
	print(round(v+e, 2))