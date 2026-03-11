from numpy import*

p = float(input("P: "))
x = array(eval(input("x: ")))
y = array(eval(input("y: ")))

t = p / (p + 1)
xt = 0
yt = 0
s1 = 0
s2 = 0
for i in range(size(x)):
	xt = xt + ((abs(x[i]))**t)**(1/t)
	yt = yt + ((abs(x[i]))**t)**(1/t)
	
print()