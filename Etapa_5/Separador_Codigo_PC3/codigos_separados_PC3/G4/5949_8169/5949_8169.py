x = str(input("Voce ira querer Bolo ou Croassant? C/B ")).upper()
q = int(input("quantos voce ira querer? "))
c = int(input("Quantos cappuccinos?"))

if (x == "C"):
	vx = 6.00
else:
	vx = 3.00
	
vt = vx * q + c * 5.50
print(vt)