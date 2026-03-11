#mnc : 1.20
#mc  : 0.90

xc = int(input("xc: "))

if xc <= 3:
	f = xc*1.20

else:
	f = xc*0.90

print(round(f,2))
