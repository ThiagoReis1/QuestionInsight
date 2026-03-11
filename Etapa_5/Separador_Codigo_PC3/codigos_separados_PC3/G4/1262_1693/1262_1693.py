from numpy import*
p = float(input("s"))
x = array(eval(input("a")))
y = array(eval(input("b")))
t = p/(p-1)
v = 0

for i in range(size(x)):
	v += abs(x[i] - y[i]) ** t
d = (v) ** (1/t)
print(round(d,6))