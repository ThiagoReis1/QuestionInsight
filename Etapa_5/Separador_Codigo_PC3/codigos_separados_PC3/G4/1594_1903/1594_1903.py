from numpy import*

v = array(eval(input("danos: ")))

i = 0
j = 1
d = 0

while(i < size(v)):
	d = d +v[i]*j
	i += 1
	j += 1
print(d)