from numpy import*
n=input().split(",")
ar=0
br=0
cl=0
co=0
uy=0
for elemento in n:
	if(elemento=='AR'):
		ar=ar+1
	elif(elemento=='BR'):
		br=br+1
	elif(elemento=='CL'):
		cl=cl+1	
	elif(elemento=='CO'):
		co=co+1	
	elif(elemento=='UY'):
		uy=uy+1
m=max(ar,br,cl)
m1=max(cl,co,uy)
if(m>m1):
	print(m)
else:
	print(m1)
k=array([ar,br,cl,co,uy])
print(k)