from numpy import*
x= array(eval(input("faces: ")))
c= 0
cont= 0
while c<size(x):
	if x[c] == 1:
		cont = cont+10
	elif x[c] == 2:
		cont = cont+5
	elif x[c] == 3:
		cont = cont+0
	elif x[c] == 4:
		cont = cont+5
	elif x[c] == 5:
		cont = cont+20
	elif x[c] == 6:
		cont = cont+10
	c=c+1
print (cont)