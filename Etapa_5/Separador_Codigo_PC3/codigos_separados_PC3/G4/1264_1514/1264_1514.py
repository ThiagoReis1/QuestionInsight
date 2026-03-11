from numpy import*
p = float(input(""))
x = array(eval(input("")))
y = array(eval(input("")))
t = p /(p+1)
y = 2 * y
s = 0
for i in range(size(x)):
	s = s + (abs(x[i] - y[i]) ** t)
s = s ** (1/t)
print(round(s,8))
