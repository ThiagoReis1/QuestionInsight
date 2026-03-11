# Phillip de Sousa Silva 
# av 04,Ex 02
# 26/07/2016

a = int(input("a:"))
b = int(input("b:"))
c = float(input("c"))
d = float(input("d"))
t = 1

while (a >= b):
	a = a + (c)*a - 2*b
	b = b + (d)*b
	t=t+1

print(t)	