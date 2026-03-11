from numpy import *
num = array(eval(input("Informe aneis acertados: ")))
i=0
pts=0

while i<size(num):
	if num[i]==1:
		pts=pts+100
		i=i+1
	elif num[i]==2:
		pts=pts+60
		i=i+1
	elif num[i]==3:
		pts=pts+20
		i=i+1
	elif num[i]==4:
		pts=pts
		i=i+1
		
print(pts)