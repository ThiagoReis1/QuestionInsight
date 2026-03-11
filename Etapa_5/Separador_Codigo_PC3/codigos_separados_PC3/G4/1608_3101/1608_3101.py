from numpy import*
d= array(eval(input("numero de pessoas: ")))
i=0
while(i != size(d)):
	if(d[i] == 75):
		d = d[i] - (d +1)
		i= i +1
print(d)