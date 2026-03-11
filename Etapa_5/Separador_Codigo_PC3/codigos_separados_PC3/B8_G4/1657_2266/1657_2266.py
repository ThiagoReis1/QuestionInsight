from numpy import*
az = 0
ca = 0
fl = 0
pa = 0
wi = 0
v = input()
v1 = v.split(",")
for i in range(size(v1)):
	if v1[i] == "AZ":
		az = az + 1
	elif v1[i] == "CA":
		ca = ca + 1
	elif v1[i] == "FL":
		fl = fl + 1
	elif v1[i] == "PA":
		pa = pa + 1
	elif v1[i] == "WI":
		wi = wi + 1
v2 = zeros(5,dtype=int)		
v2[0] = az
v2[1] = ca
v2[2] = fl
v2[3] = pa
v2[4] = wi
print(max(v2))
print(v2)