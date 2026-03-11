from numpy import*

t= array(eval(input("")))
i=0
g= t[0]

while (size(t) > i):
	if t[i] == min (t):
		g= i
	i=i+1

print (g)