from numpy import *

s = input("").upper().split(',')

az= 0
ca= 0
fl= 0
pa= 0
wi= 0

for i in range(size(s)):
	if s[i] == "AZ":
		az = az + 1
	elif s[i] == "CA":
		ca = ca + 1
	elif s[i] == "FL":
		fl = fl + 1
	elif s[i] == "PA":
		pa = pa + 1
	elif s[i] == "WI":
		wi = wi + 1
		
vz = zeros(5,dtype=int)

vz[0] = az
vz[1] = ca
vz[2] = fl
vz[3] = pa
vz[4] = wi
print(max(vz))
print(vz)
