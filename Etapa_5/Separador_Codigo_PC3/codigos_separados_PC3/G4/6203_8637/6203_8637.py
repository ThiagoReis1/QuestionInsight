am = 1.4
tx = 0.06
c=0
al=float(input())
qt=float(input())


while am<al:
	al=al+qt
	am=am+tx
	c=c+1
	
print(c)