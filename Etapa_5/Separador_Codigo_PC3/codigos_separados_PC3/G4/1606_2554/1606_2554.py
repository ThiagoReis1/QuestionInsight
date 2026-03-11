from numpy import *
andar=array(eval(input("andares que parou: ")))
#ant=abs(andar[0]-andar[1])
#annt=abs(andar[1]-andar[2]-ant)
ant=0
i=0
ii=1
while(size(andar)-1>i):
	if(andar[ii]>andar[i]):
		ant=abs(andar[ii]-andar[i]+ant)
		i=i+1
		ii=ii+1
	else:
		ant=abs(andar[i]-andar[ii]+ant)
		i=i+1
		ii=ii+1
print(ant)


	