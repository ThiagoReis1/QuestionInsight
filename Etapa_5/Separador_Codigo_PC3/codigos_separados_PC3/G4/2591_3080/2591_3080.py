from numpy import*

v= array(eval(input()))

vra=0 #variavel acumuladora

for x in range(size(v)):
	if( x <= v[0]):
		vra= vra + 1
	print(vra)