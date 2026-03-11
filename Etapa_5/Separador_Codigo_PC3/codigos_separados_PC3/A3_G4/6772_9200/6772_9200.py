c = float(input("digite c: "))
p = input("DPC1C2: ").upper()

if (p == "D"):
	v1 = (c*0.83)
	print(round(v1,2))

elif (p == "P"):
	v2 = (c*0.83)
	print(round(v2,2))
	
elif (p == "C1"):
	v3 = (c*1)
	print(round(v3,2))
	
else:
	t = (p == "C2")
	v4 = (c*1.08)
	print(round(v4,2))