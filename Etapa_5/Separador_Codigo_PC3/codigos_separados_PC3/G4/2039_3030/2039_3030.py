nuc = input("qual e o nucleotidio?")
a = 0
while(nuc.upper() != "S"):
	if(nuc.upper() == "A"):
		a = a+1
	nuc = input("qual e o nucleotidio?")

print(a)