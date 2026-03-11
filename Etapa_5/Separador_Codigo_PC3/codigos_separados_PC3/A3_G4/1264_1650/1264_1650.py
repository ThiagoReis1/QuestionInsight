from numpy import*

p = float((input("valores de p: ")))
x = array(eval(input("valores de x: ")))
y = array(eval(input("valores de y: ")))
h=0
n=0
j=0
q = (p/(p+1))
xy= (x - (2*y))
for i in xy:
	n = n + (abs(i))**q
v= n ** (1/q)
print(round(v,8))