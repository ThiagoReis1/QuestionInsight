from numpy import*

a = str(input()).upper()
v = a.split(',')
vet_z = zeros(5,dtype=int)

az = 0
ca = 0 
fl = 0
pa = 0
wi = 0 

for i in range(size(v)):
	
	if v[i] == "AZ": 
		az += 1 
	elif v[i] == "CA":
		ca += 1
	elif v[i] == "FL":
		fl += 1
	elif v[i] == "PA":
		pa += 1
	elif v[i] == "WI":
		wi += 1
	
vet_z[0] = az
vet_z[1] = ca
vet_z[2] = fl
vet_z[3] = pa
vet_z[4] = wi

print(max(vet_z))
print(vet_z)