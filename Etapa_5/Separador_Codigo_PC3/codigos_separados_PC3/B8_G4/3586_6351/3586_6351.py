from numpy import*
v = array(eval(input("digite o vetor: ")))
i = 0
pt = 0 
while(i<size(v)):
	if(v[i]==1):
		s = 100
		pt = pt + s
	elif(v[i]==2):
		s = 60
		pt = pt + s
	elif(v[i]==3):
		s = 20
		pt = pt + s
	elif(v[i]==4):
		s = 0
		pt = pt + s
	i = i + 1
print(pt)