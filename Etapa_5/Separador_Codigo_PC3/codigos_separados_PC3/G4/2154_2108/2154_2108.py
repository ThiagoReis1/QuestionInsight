from numpy import*
x = array(eval(input("ss:")))

m = mean(x)
p = 1
for i in x:
	p = p * (abs(i - m) ** (1/size(x)))
print(round(p,3))