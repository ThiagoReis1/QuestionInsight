from numpy import *

s = input("Digite: ")
sx = s.split(",")

BE=0
ES=0
FR=0
IT=0
PT=0

x = zeros (5,dtype= int)

for s in sx:
	if(s== "BE"):
		BE+=1
	elif(s=="ES"):
		ES+=1
	elif(s=="FR"):
		FR+=1
	elif(s=="IT"):
		IT+=1
	elif(s=="PT"):
		PT+=1
		
x[0] = BE
x[1] = ES
x[2] = FR
x[3] = IT
x[4] = PT

print(max(x))
print(x)