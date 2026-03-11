from numpy import*

n = array(eval(input()))
i = 0

while(i < size(n)):
	if(n[i]>80):
		n[i] = n[i] - n[i]*(15/100)
	i = i + 1
print(round(sum(n),2))