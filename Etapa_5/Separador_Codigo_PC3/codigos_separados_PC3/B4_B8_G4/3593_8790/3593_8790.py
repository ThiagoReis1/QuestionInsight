from numpy import*

d = array(eval(input()))

i = 0
cont = 200
 
while i<size(d):
	if d[i]==1:
		cont= cont/2
	elif d[i]==2:
		cont= cont*3
	elif d[i]==3:
		cont = cont/2
	elif d[i]==4:
		cont = cont*3
	elif d[i]==5:
		cont = cont/2
	elif d[i]==6:
		cont = cont*3
	i = i+1
print(round(cont,2))