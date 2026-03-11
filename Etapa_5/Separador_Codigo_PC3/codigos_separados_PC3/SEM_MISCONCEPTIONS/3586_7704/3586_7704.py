from numpy import*

aneis= array(eval(input()))

i= 0
pt= 0

while i <size(aneis):
	if aneis[i] == 1:
		pt+=100
	if aneis [i]== 2:
		pt+=60
	if aneis[i]==3:
		pt+=20
	if aneis[i]==4:
		pt+=0
	i+=1
		
print(pt)