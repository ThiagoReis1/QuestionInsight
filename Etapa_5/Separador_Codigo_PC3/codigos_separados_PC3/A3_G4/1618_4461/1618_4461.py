from numpy import*

v = " "
u = array(eval(input("vetor: ")))
cont = 0
m = 1
x = " "
y = size(u) - m
while(cont<size(u)):
	y = size(u) - m
	if(y == 1):
		x = str(x) + str(u[cont]) + "x" + " + "
	elif(y == 0):
			x = str(x) + str(u[cont])
	else:
		x = str(x) + str(u[cont]) + "x^" + str(size(u) - m) + " + "
	
	m = m +1
	cont = cont +1



print(x)
