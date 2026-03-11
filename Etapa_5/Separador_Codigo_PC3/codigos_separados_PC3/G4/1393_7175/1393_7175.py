f=float(input("peso da encomenda:"))
if(f<5000):
	x=f*0.05
else:
	x=(f*0.04)+60
print(round(x,2))


