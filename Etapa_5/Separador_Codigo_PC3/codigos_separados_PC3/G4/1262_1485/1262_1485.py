from numpy import*
p = float(input("digite p: "))
x = array(eval(input("digite x: ")))
y = array(eval(input("digite y: ")))
l = 0
t = (p/(p-1))
xy = (x - y)
for i in xy:
	l = l + (abs(i))**t
v = l**(1/t)
print (round(v,6))
