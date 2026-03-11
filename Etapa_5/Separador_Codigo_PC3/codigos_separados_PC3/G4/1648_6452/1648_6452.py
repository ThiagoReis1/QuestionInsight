from numpy import*
presenca=array(eval(input()))
rep=0
for i in range (size(presenca)):
	if presenca[i]<70:
		rep=rep+1
t=zeros(rep,dtype=int)
g=0
for i in range(size(presenca)):
	if presenca[i]<70:
		t[g]=i
		g=g+1
print(rep)
print(t)
	