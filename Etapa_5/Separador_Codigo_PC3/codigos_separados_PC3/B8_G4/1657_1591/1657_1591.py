from numpy import *

s = input("Digite: ")
sx = s.split(",")

AZ=0
CA=0
FL=0
PA=0
WI=0

x = zeros (5,dtype= int)

for s in sx:
	if(s== "AZ"):
		AZ+=1
	elif(s=="CA"):
		CA+=1
	elif(s=="FL"):
		FL+=1
	elif(s=="PA"):
		PA+=1
	elif(s=="WI"):
		WI+=1
		
x[0] = AZ
x[1] = CA
x[2] = FL
x[3] = PA
x[4] = WI

print(max(x))
print(x)