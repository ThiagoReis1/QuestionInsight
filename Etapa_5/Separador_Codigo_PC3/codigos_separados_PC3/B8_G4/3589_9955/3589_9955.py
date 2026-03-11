from numpy import *

an=array(eval(input()))

idc=0
ppt=0

while idc<size(an):
	if an[idc]==1:
		ppt+=80
	elif an[idc]==2:
		ppt+=40
	elif an[idc]==3:
		ppt+=20
	elif an[idc]== 4:
		ppt+=10
	idc+=1
print(round(ppt,2))