from numpy import*
v = array(eval(input("vetor:")))
i=1
n=0
while(i<size(v)):
	if(v[i]==min(v)):
		n  = i
	i=i+1
print(n)