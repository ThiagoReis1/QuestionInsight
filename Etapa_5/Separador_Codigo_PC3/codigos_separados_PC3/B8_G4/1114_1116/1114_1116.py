v = float(input("Velocidade: "))
h = float(input("Tempo: "))
s = v * h
dac = 100
dce = 200
dEf = 150
dfg = 400
dgh = 250
dt = dac + dce + dEf + dfg + dgh
ho = dt / v
if(ho < h):
	ho = "Hogsmead"
	print("Entradas: ", v,"km/h e", h,"h")
	print("Proxima parada:", ho)
elif(v <= 0 or h <= 0):
	print("Entradas: ", v,"km/h e", h,"h")
	print("Dados Invalidos")
else:
	if(s <= dac):
		c = "Castamere"
		print("Entradas: ", v,"km/h e", h,"h")
		print("Proxima parada: ",c)
	elif(s >= dac and s <= dce):
		e = "Edoras"
		print("Entradas: ", v,"km/h e", h,"h")
		print("Proxima parada: ",e)
	elif(s >= dEf and s <= dfg):
		f = "Farnagon"
		print("Entradas: ", v,"km/h e", h,"h")
		print("Proxima parada: ",f)
	elif(s >= dfg and s <= dgh):
		g = "Gondor"
		print("Entradas: ", v,"km/h e", h,"h")
		print("Proxima parada: ",g)
	elif(s >= 0 and s == dt or s <= dfg and s >= dgh):
		ho = "Hogsmead"
		print("Entradas: ", v,"km/h e", h,"h")
		print("Proxima parada: ",ho)



