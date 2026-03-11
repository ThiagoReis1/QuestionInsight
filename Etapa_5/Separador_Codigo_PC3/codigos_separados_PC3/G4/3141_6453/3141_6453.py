from numpy import*


p = array(eval(input("p: ")))

i = 0 
t = 0 
while(i < size(p)):
	t = t + p[i]**(1/6)
	i = i + 1
m = (t/size(p))**6
print(round(m, 2))  