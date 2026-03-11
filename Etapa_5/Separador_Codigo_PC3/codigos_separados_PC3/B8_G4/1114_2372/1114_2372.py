vel = float(input())
time = float(input())
# time > 250 km entao temos Hogsmead
# time < 100 ou time = 0 ou time < 0 entao temos uma invalidez
km = vel * time
print("Entradas:", vel, "km/h e", time, "h")
if(km > 1400):
	print("Proxima parada: Hogsmead")
elif(km == 100):
	print("Proxima parada: Castamare")
elif(km == 200):
	print("Proxima parada: Doriath")
elif(km == 400):
	print("Proxima parada: Edoras")
elif(km == 600):
	print("Proxima parada: Fangorn")
elif(km == 750):
	print("Proxima parada: Gondor")
elif(vel < 0 or vel == 0 or time < 0):
	print("Dados invalidos")