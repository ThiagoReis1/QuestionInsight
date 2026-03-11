from numpy import*
p = float(input("numero:"))
x = array(eval(input("dalhe man:")))
y = array(eval(input("vain:")))

t = p / (p-1)

x = 2 * x
y = 3 * y
s = 0
for i in range(size(x)):
	s = s +(abs(x[i] + y[i]) ** t)
s = s ** (1/t)			  
print(round(s, 3))			  