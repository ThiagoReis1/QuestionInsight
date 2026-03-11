v = float (input())
t = float (input())
s = v * t
print("Entradas:", v, "km/h e", t, "h")
if (v > 0 and t > 0):
	if(s < 100):
		x = "Avalon"
	elif(s >= 400 and s < 600): 
		x = "Doriath"
	elif(s >= 200 and s < 400):
		x = "Castamare"
	
	print("Proxima parada:", x)
else:
	print("Dados invalidos")