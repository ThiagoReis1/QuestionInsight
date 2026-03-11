from numpy import*
x= array(eval(input("")))
p = 10000
i = 0
while i < size(x):
	if x[i] == 1:
		p = p *2
	if x[i]==2:
		p = p
	if x[i]==3:
		p= p/2
	if x[i]==4:
		p = p/4
	i = i+1
print(round(p,2))
