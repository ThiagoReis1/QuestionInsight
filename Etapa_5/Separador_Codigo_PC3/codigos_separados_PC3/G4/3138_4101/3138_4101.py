from numpy import*
v = array(eval(input("v: ")))
n = size(v)
i=0
m1=0
while(i<(n)):
	m1 = m1 + (v[i]**7)
	i = i + 1
m = (m1/n)**(1/7)
print(round(m,  2))