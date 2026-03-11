from numpy import*
v=input("").split(',')
q=zeros(5,dtype=int)
br=0
ar=0 
cl=0         #GG WP#0 0
co=0               # ¬
uy=0   
n=0
for x in v:
	if x == "AR":
		ar=ar+1
		
	elif x=="BR":
		br=br+1
		
	elif x=="CL":
		cl=cl+1
		
	elif x=="CO":
		co=co+1
		
	elif x=="UY":
		uy=uy+1
		
q[0]=ar
q[1]=br
q[2]=cl
q[3]=co
q[4]=uy
print(max(q))
print(q)