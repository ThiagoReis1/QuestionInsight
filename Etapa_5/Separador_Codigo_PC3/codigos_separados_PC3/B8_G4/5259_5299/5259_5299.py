v = float(input(""))
n = int(input(""))

if (n ==1):
	x = 0.90*v
	y = x*n
	print(round(y,2))
elif(n==2):
	t = 0.70*v
	i = t*n
	print(round(i,2))
elif(n >= 3):
	z =  0.60*v
	j = z*n
	print(round(j,2))