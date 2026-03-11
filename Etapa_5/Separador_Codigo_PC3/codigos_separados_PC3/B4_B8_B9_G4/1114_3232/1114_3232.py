v = float(input("v: "))
t = float(input("t: "))
s = v * t
print("Entradas :", v, "km/h e", t, "h")
if(v > 0 and t > 0):
	if(s < 100):
		x = "Avalon"
	elif(s >= 100 and s < 200):
		x = "Bravo"
	elif(s >= 200 and s < 400):
		x = "Castamere"
	elif(s >= 200 and s < 400):
		x = "Castamere"
	
	print("Proxima parada:", x)
else:
	print("Dados invalidos")