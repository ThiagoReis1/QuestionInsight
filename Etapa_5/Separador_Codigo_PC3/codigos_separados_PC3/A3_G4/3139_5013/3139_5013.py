from numpy import*

n = array(eval(input(": ")))

m = 0 #media
j = 0
i = 0
while(i < size(n)):
	j = n[i]**(1/3) + j
	i = i + 1
m = (j/size(n))**3
print(round(m, 2))