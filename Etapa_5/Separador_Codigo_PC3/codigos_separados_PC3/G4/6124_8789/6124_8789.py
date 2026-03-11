x = float(input())

if (x>=3000) and (x<3400):
	z= x*0.8
	print(round(z,1))
elif (x>=3400) and (x<3900):
	z = x*1.3
	print(round(z,1))
elif (x>=3900) and (x<4100):
	z = x* 2.1
	print(round(z,1))
else :
	z= x * 3
	print(round(z,1))