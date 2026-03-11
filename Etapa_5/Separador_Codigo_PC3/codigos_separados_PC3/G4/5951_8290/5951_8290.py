esc = input("Tapioca ou salgado: ").upper()
qesc = int(input("quantidade: "))
qa = int(input("quantidade de acais: "))

if (esc == "T"):
	vt = (qesc * 4.50) + (qa * 12)
	
else:
	vt = (qesc * 5) + (qa * 12)
	
print(vt)
