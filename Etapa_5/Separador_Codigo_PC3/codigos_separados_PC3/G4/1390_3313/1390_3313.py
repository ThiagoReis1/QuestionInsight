minu = float(input("minutos: "))
x = minu * 1.20
y = 25.0 + (minu * 1.40)
if(minu<=100):
	print(round(x,2))
else:
	print(round(y,2))