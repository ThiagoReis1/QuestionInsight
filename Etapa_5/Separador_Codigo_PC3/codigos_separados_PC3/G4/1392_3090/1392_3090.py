ca = float(input("Consumo de agua: ")) 
if	(ca < 10):
	msg = 30 + (3 * ca)
else:
	msg = 30 + (3.5 * ca)
print(round(msg,2))