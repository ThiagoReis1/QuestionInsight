p = float(input("peso"))
d = float(input("distancia"))
c = float(input("codigo"))

ckg = 25
ckm = 0.1

pts = ((p * ckg) + (d*ckm)) * (1 + (icms/100))

#print(round(pts, 2))

if(icms == 17):
	
