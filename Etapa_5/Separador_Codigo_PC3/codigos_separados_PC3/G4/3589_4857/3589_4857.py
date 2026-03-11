from numpy import*

v = array(eval(input("Digite os numeros: ")))
c = 0 
for i in range(size(v)):
	if v[i] == 1:
		c = c+ 80
	elif v[i] == 2:
		c = c +40
	elif v[i] == 3:
		c= c+ 20
	else:
		c = c+10
print(c)