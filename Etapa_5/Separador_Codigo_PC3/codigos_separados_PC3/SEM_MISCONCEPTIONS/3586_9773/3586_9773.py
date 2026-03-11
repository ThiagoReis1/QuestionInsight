from numpy import*
aneis=array(eval(input()))
i=0
pts=0
while i < size(aneis):
	if aneis[i]==1:
		pts+=100
	if aneis[i]==2:
		pts+=60
	if aneis[i]==3:
		pts+=20
	if aneis[i]==4:
		pts+=0
	i+=1
print(pts)