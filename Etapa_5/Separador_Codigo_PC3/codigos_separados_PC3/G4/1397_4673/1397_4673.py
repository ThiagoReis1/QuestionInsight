a=float(input("area  a ser fertilizada:"))
if(a<=10000):
	c=(5 * a)
else:
	c=(5 *10000)+ 4 *(a - 10000)
print(round(c,2))
