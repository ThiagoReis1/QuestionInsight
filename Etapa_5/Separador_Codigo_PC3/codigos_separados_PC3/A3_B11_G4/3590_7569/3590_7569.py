from numpy import*
d = array(input("vetor_num: "))
i = 0
b = 0
while(i<size(d)):
	if(d[i]==1):
		v = i+10
	if(d[i]==2):
		v = i+5
	if(d[i]==3):
		v = i
	if(d[i]==4):
		v = i+5
	if(d[i]==5):
		v = i+20
	if(d[i]==6):
		v = i+10
		b = b+1
	print(v)