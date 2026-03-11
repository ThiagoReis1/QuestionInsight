from numpy import*
v = array(eval(input("insira o v: ")))
i = 0
m = 0
while(i<size(v)):
	m = m +((float(v[i]))**(1/3))
	i = i + 1
x = (m/size(v))**3
print(round(x,2))


