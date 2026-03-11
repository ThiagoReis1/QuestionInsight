from numpy import*

t = array(eval(input("tempo no banho: ")))
a = array(eval(input("percentual da abertura: ")))
g = 0
for i in range(size(a)):
	if(a[i]!=0):
		g = g + (a[i]/100*5*t[i])
		
print(g)