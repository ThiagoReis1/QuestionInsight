from numpy import *
a = input ("").upper()
v = a.split(",")
vt_z = zeros(5,dtype=int)
ar=0
br=0
cl=0
co=0
uy=0
for i in range(size(v)):
	if v[i] == "AR":
		ar+=1
	elif v[i] == "BR":
		br+=1
	elif v[i] == "CL":
	   cl+=1
	elif v[i] == "CO":
		co+=1
	elif v[i] == "UY":
		uy+=1
vt_z[0]=ar
vt_z[1]=br
vt_z[2]=cl
vt_z[3]=co
vt_z[4]=uy
print(max(vt_z))
print(vt_z)
	
	