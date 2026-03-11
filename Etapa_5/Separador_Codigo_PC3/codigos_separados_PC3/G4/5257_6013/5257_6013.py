p = float(input())

if (p<=50):
	x = 2*p
	print(round(x,2))
elif (p>=50.01) and (p<=100):
	x=(p+0.5*p)
	print(round(x,2))
elif (p>=100.01) and (p<=500):
	x = (p+0.4*p)
	print(round(x,2))
else:
	x = (p*0.3) + p
	print(round(x,2))
	

	