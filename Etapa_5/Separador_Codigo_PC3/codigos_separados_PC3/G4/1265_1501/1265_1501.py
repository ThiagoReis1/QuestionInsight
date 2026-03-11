from numpy import*
p = float(input(""))
x = (array(eval(input(""))))
y = (array(eval(input(""))))
t = p / (p -1)
v = 0
for i in range(0, size(x)):
	 v += abs(2*x[i] + 3*y[i]) ** t
d= (v) ** (1/t)
print(round(d,3))