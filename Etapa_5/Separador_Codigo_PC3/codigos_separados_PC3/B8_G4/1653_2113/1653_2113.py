from numpy import*
n=input("nacionalidade: ").split(',')
ar=0
br=0
cl=0
co=0
uy=0
for i in n:
	if(i=="AR"):
		ar=ar+1
	elif(i=="BR"):
		br=br+1
	elif(i=="CL"):
		cl=cl+1
	elif(i=="CO"):
		co=co+1
	elif(i=="UY"):
		uy=uy+1
s=array([ar,br,cl,co,uy])
print(max(s))
print(s)
