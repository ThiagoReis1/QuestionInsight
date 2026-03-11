from numpy import*
d= array(eval(input("numero dos dados:")))

k= len(d)
i= 0
c= 200

while i<k:
	if d[i]== 1:
		c = c/2
	elif d[i]== 2:
		c= c*3
	elif d[i]==3:
		c= c/2
	elif d[i]==4:
		c=c*3
	elif d[i] == 5:
		c= c/2
	elif d[i]==6:
		c=c*3
	i=i+1
print(round(c,2))