pc= float(input("  leia o peso da encomenda:"))

if (pc<5000):
	print(round(pc*0.05, 2 ))
else:
	print(round((pc*0.04) + 60, 2))
	