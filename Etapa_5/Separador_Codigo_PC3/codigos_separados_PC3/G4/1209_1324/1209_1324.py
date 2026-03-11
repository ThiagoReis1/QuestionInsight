from numpy import*

re= 74.08
disc= array(eval(input()))
i=0
c=0
while (i<size(disc)):
	if (disc[i]>re):
		c = c+1
	i+=1
print(re)
print(c)