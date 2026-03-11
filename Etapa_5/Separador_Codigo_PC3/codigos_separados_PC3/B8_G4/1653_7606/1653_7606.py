from numpy import *
v= input("digite").upper().split(',')
ar = 0
br = 0 
cl = 0
co = 0
uy = 0
for i in range(size(v)):
	if v[i] == "AR":
		ar = ar + 1
	elif v[i] == "BR":
		br = br + 1
	elif v[i] == "CL":
		cl = cl + 1
	elif v[i] == "CO":
		co = co + 1
	elif v[i] == "UY":
		uy = uy + 1	

#print(     array([ar,br,cl,co,uy]     ))

x = array([ar,br,cl,co,uy])
print(max(x))
print(x)



		