x = float(input("x: "))
k = int(input("k: "))

p = 1
fim = k
while(p<fim):
	p = p + 1
	d = 1 + ((-1)**p)*(x**p)
if(x >= 0):
	print(round(d, 7))
elif(x<0):
	d = 1 + ((-1)**p)*(x**p)/(-1)
	print(round(d, 7))