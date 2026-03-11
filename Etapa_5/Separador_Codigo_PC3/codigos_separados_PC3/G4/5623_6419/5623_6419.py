fb = 5.00
s = 4.00
c = 7.50
o = input("Digite B/S: ")
q = int(input("Digite a quantidade: "))
qc = int(input("Digite a quantidade de cappuccino: "))

if o == "B":
	vt = fb * q + c * qc
	print(vt)
if o == "S":
	vt = s * q + c *qc
	print(vt)
	
	
	