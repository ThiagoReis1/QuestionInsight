face= int(input('face;'))

x=0
s=0
while(face!=-1):
	x=x+1
	if(face == 6):
		s=s+1
	face= int(input('face:'))

	
p= (s-x)*-1
z= p*100/x


print(x)
print (round(100-z,2))