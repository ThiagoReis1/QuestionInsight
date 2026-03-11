from numpy import *

st = input()

p = 0
c = 0
m = 0
v = 0
a = 0

vet = st.split(',')
vet2 = zeros(5,dtype=int)

for i in vet:
	if(i == "P"):
		vet2[0] = vet2[0] + 1
	elif(i == "C"):
		vet2[1] = vet2[1] + 1	
	elif(i == "M"):
		vet2[2] = vet2[2] + 1
	elif(i == "V"):
		vet2[3] = vet2[3] + 1
	else:
		vet2[4] = vet2[4] + 1	

print(max(vet2))				
print(vet2)
