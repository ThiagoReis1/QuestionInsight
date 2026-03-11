r = input("Resultado: ").upper()
po = 0
s = 0
while (r != "X"):
	if (r == "V"):
		po = po + 3
	if (r == "E"):
		po = po + 2
	if (r == "D"):
		po = po + 1
	r = input("Resultado: ").upper
	s = s+1 
	pp = s*3
p = (pp/po)*100
print(p)
