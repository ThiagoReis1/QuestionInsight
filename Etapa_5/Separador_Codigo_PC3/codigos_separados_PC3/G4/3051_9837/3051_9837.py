x = float(input("digite um valor:"))

if (x>=0) and (x<=150):
	v = x*0.60+5.0
	print(round(v, 2))
elif (x>=150) and (x<=250):
	v = x*0.65+8.0
	print(round(v, 2))
elif (x>=250) and (x<=350):
	v = x*0.70+12.0
	print(round(v, 2))
else:
	v = x*0.75+16.0
	print(round(v, 2))