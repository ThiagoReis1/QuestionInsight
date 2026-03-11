from numpy import*

nts=array(eval(input("")))
ps=[3,5,1]

c=0
nt=0

while c<3:
	nt+=nts[c]*ps[c]
	c+=1
	
print(round(nt/sum(ps),2 ))
