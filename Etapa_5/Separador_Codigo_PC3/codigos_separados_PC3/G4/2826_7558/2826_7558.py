from numpy import* 
v = array(eval(input("nota: ")))
i = 0 
while v[i] <= 2:
	v[i] = v[i] - v[i]
	i +=  1
print(v)