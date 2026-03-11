from numpy import*
l=array(eval(input("<3   ")))
p=array(zeros(size(l)),dtype(int))
cont=0
for e in l:
	if(e<50):
		p=p+[e]
		cont=cont+1
print(cont)
