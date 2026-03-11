v = float(input("valor consumido: "))

if(v <= 300.0):
	gorjeta = (10/100) * v 
	v_t = gorjeta + v
	print (round(v_t, 2))
else:
	gorjeta = (6/100) * v
	v_t = gorjeta + v
	print (round(v_t, 2))