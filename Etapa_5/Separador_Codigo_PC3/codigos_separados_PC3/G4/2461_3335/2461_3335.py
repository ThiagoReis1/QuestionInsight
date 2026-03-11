p = float(input("Valor do produto: "))

if(p <=50):
	ml = 1*p
	vt = p+ml
elif(50.01<=p<=100):
	ml = (50/100)*p
	vt = p+ml
elif(100.01<=p<=500):
	ml = (40/100)*p
	vt = p+ml
else:
	ml = (30/100)*p
	vt = p+ml
print(round(vt,2))