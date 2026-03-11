from numpy import*
t = array(eval(input("qual valor de cada produto que vc comprou?")))
i=0
desc = 0
while(i<size(t)):
	if(t[i]>80):
		desc = desc - 5
		i=i+1
	else:
		i=i+1
vt = sum(t)+desc
print(round(vt,2))