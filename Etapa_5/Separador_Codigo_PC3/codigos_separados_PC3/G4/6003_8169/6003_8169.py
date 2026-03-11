c = int(input("Quantas cenoras foram compradas?"))

if (c<5):
	vlr = 1.20
else:
	vlr = 0.90
	
vt = c * vlr
print(round(vt,2))