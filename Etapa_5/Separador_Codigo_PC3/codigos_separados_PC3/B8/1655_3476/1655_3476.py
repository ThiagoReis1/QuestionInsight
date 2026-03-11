from numpy import*
x=input("Digite x: ")
vet = x.split(',')
vresp = zeros(5,dtype=int)

for cont in vet:
	if(cont.upper()=="AC"):
		vresp[0]=vresp[0]+1
	elif(cont.upper()=="AM"):
		vresp[1]=vresp[1]+1
	elif(cont.upper()=="PA"):
		vresp[2]=vresp[2]+1
	elif(cont.upper()=="RO"):
		vresp[3]=vresp[3]+1
	elif(cont.upper()=="RR"):
		vresp[4]=vresp[4]+1
print(max(vresp))
print(vresp)