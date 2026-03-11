from numpy import*

vs=array(eval(input()))
v=array(eval(input()))

i=0
c=0
f=0
dw=0
e=0
da=0

while(i<size(vs)):
	if(vs[i]=="CENOURA"):
		d=2 * v[i]
		c= c + d
	elif(vs[i]=="FERRO"):
		d= 4 * v[i]
		f= f + d
	elif(vs[i]=="DWARVEN"):
		d= 8 * v[i]
		dw= dw + d
	elif(vs[i]=="ELVEN"):
		d= 11 * v[i]
		e= e + d
	elif(vs[i]=="DAEDRIC"):
		d= 14 * v[i]
		da= da + d
	i= i + 1

t= c + f + dw + e + da
print(t)
	