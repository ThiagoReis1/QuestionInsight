from numpy import*

v = array(eval(input("100% fe: ")))
cont = 0
for i in range(size(v)):
	cont = cont + v[i]
	if(v[i] == 99):
		cont = cont* 2		
print(cont)	