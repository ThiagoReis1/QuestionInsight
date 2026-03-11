from numpy import *
nt=array(eval(input("notas:  ")))
i=0
p=0
sn=0
d=0
while(i<size(nt)):	
	p=p+1
	d=d+p
	sn=sn+(nt[i]*p)
	i=i+1

mp=sn/d
print(round(mp, 2))