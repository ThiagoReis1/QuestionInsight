from numpy import*

v=array(eval(input( )))

acum=0

for i in v:
	if v[i]>(6/5)*v[0] and v[i]<(1/2)*v[0]:
		print(i)
		acum=acum+1
print(acum)
	