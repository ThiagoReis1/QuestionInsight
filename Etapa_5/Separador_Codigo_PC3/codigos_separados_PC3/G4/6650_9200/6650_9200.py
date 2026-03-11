from numpy import*

n = array(eval(input("digite: ")))
p = [4,3]
i = 0
x = 0

while(i < size(n)):
	x = x +(n[i]*p[i])/7
	i = i + 1

print(round(x,2))