v=float(input())
t=float(input())
print("Entradas:", v,"km/h e", t,"h")
if(t>0 and v>0):
	if(v*t<100):
		print("Proxima parada: Bravos")
	elif(v*t>=100 and v*t<200):
		print("Proxima parada: Castemere")
	elif(v*t>=200 and v*t<400):
		print("Proxima parada: Doriath")
	elif(v*t>=400 and v*t<600):
		print("Proxima parada: Edoras")
	elif(v*t>=600 and v*t<750):
		print("Proxima parada: Fangorn")
	elif(v*t>=750 and v*t<1150):
		print("Proxima parada: Gondor")
	elif(v*t>=1150 and v*t<1400):
		print("Proxima parada: Hogsmead")
else:
	print("Dados invalidos")