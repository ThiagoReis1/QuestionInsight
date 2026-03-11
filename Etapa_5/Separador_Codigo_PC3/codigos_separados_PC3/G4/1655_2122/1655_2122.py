from numpy import*
from numpy import*
s= input(": ").upper()
ac=0
am=0
pa=0
ro=0
rr=0
j= s.split(",")
z= zeros(5, dtype=int)
i=0
for i in j:
	if(i.upper() == 'AM'):
		am=am+1	
		z[1]= am
	if(i.upper() == 'AC'):
		ac=ac+1
		z[0]=ac
	if(i.upper() == 'PA'):
		pa=pa+1
		z[2]= pa
	if(i.upper() == 'RO'):
		ro=ro+1
		z[3]=ro
	if(i.upper() == 'RR'):
		rr=rr+1
		z[4]= rr
print(max(z))
print(z)
