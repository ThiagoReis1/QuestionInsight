e = input("escala?").upper()
t = float(input("temperatura"))
if e == "C":
   a = (t+273.15)
else:
   a = (t-273.15)
	
print(round(a, 2))

	

	