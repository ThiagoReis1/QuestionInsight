from numpy import*

y= array(eval(input("insira: ")))
p=10000
i=0

while i<size(y):
	if y[i] == 1:
		p= p*2
	elif y[i] == 2:
		p=p
	elif y[i] == 3:
		p=p/2
	elif y [i] ==4:
		p=p/4
	i=i+1
print(round(p,2))