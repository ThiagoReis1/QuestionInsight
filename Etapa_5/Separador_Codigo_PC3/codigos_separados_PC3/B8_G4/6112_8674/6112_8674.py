cc = float(input())

if cc < 17.5:
	a = cc + 10.5
	print(round(a , 2))
elif (cc < 17.5 or cc < 35.0):
	a = cc + 14.0
	print(round(a , 2))
elif (cc < 35.0 or cc < 50.0):
	a = cc + 18.6
	print(round(a , 2))
elif cc > 50.0:
	a = cc + 24.5
	print(round(a , 2))