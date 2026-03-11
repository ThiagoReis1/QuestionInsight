x=float(input(" valor "))

if x<=1:
	print(round(1,2))
	
elif (x<1) or (x<=2):
	print(round(2,2))
	
elif (2<x) and (x<=3):
	y=x**2
	print(round(y,2))
	
else:
	w=x**3
	print(round(w,2))