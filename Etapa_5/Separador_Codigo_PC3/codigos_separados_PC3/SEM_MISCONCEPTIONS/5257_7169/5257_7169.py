c = float(input("custo"))
if(c < 50):
	a = c*0.10+c
	print(round(a+c,2))
	if(c > 50.01):
		b = c*0.50+c
		print(round(c+b, 2))
	elif(c > 100.01):
		m = c*0.40+c
		print(round(m=c, 2))
if(c > 500):
	k = c*0.30+c
	print(round(k+c, 2))