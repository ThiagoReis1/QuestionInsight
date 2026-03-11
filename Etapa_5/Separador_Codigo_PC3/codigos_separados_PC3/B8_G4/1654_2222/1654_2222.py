from numpy import*
a=input("estados: ").split(',')

z = zeros(5, dtype=int)

for i in range(len(a)):
	if(a[i]=="AM"):	
		z[0]=z[0]+1
	elif(a[i]=="PE"):
		z[1]=z[1]+1
	elif(a[i]=="MG"):
		z[2]=z[2]+1
	elif(a[i]=="SP"):
		z[3]=z[3]+1
	elif(a[i]=="RS"):
		z[4]=z[4]+1
		
print(max(z))
print(z)
		