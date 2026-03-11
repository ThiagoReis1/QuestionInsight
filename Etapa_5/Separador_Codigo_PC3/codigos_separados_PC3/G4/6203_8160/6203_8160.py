am = 1.4
tm = 0.06
al= float(input('altura: '))
tl= float(input('taxa: '))
c=0
while(am<=al):
	am=am+tm
	al=al+tl
	c=c+1
print(c)