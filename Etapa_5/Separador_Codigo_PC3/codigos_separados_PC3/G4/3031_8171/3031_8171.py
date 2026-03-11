x=float(input(""))

if x<=1:
	fx=1
elif x<=2:
	fx=2
elif x<=3:
	fx=x**2
else:
	fx=x**3
print(round(fx,2))