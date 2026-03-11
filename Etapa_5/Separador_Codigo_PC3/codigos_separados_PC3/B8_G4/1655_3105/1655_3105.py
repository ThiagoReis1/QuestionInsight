estados=input("").split(',')
from numpy import*
ac=0
am=0
pa=0
ro=0
rr=0
vz=zeros(5,dtype=int)
for i in range(size(estados)):
	if (estados[i]=="AC"):
		ac=ac+1
	elif(estados[i]=="AM"):
		am=am+1
	elif(estados[i]=="PA"):
		pa=pa+1
	elif(estados[i]=="RO"):
		ro=ro+1
	elif(estados[i]=="RR"):
		rr=rr+1
vz[0]=ac
vz[1]=am
vz[2]=pa
vz[3]=ro
vz[4]=rr
print(max(vz))
print(vz)
		
	
