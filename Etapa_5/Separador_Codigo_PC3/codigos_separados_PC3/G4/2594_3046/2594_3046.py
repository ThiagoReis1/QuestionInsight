from numpy import *
vd = array(eval(input("v: ")))

acum = 0
for i in range(size(vd)):
	if(vd[i] > vd[0]):
		acum = acum + 1
		print(i)
print(acum)
