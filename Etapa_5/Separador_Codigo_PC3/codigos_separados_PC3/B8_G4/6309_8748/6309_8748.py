from numpy import*
sigla = input("H, C ou L: ").upper()
i = 0
cont = 0
h = 0
c = 0
l = 0

while i < len(sigla):
	if sigla[i] == "H":
		cont = cont + 5.4
		h = h + 1
	elif sigla[i] == "C":
		cont = cont + 8.95
		c = c + 1
	elif sigla[i] == "L":
		cont = cont + 4.5
		l = l + 1
	i = i + 1
	
print(round(cont,2))
print(h,c,l)
