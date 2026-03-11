from numpy import*
vet = array(input(":").split(","))

z = zeros(5,dtype=int)
az = 0
ca = 0
fl = 0
pa = 0
wi = 0
for i in vet:
	if(i == "AZ"):
		az = az + 1
	elif(i == "CA"):
		ca = ca + 1
	elif(i == "FL"):
		fl = fl + 1
	elif(i == "PA"):
		pa = pa + 1
	elif(i == "WI"):
		wi = wi + 1
z[0] = az
z[1] = ca
z[2] = fl
z[3] = pa
z[4] = wi
print(max(z))
print(z)