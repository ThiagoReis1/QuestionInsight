from numpy import*
x = array(eval(input("")))
p = 0
i = 0
while i < size(x):
	if x[i]==1:
		p += 80
	if x[i]==2:
		p += 40
	if x[i]==3:
	   p += 20
	if x[i]== 4:
		p += 10
	i = i+1

print(p)