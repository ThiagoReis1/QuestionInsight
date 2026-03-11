am = 1.86
tm = 0.01
ac=float(input("altura do coelho: "))
tc=float(input("taxa do coelho: "))
c=0
while(ac<=am):
	ac=ac+tc
	am=am+tm
	c=c+1
print(c)
