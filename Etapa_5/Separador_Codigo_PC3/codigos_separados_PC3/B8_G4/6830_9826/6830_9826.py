from numpy import*
c = input("digite a secao: ").upper()
hf = 3.85
lac = 2.95
enl = 7.90

nm_hf = 0
nm_lac = 0
nm_enl = 0
i = 0 

while i < len(c):
	prod = c[i]
	if prod == "H":
		nm_hf += 1
	elif prod == "L":
		nm_lac += 1
	elif prod == "E":
		nm_enl += 1
	i += 1
vf = (nm_hf * hf) + (nm_lac * lac) + (nm_enl * enl)
print(round(vf, 2))