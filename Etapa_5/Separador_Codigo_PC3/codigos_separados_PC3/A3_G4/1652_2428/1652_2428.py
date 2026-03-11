from numpy import*

st = input()
b = 0
pa = 0
pr = 0
a = 0
i = 0

vet = st.split(',')
vet2 = zeros(5,dtype=int)
for i in vet:
	if (i == "B"):
		vet2[0] = vet2[0] + 1
	elif (i == "PA"):
		vet2[1] = vet2[1] + 1
	elif (i == "PR"):
		vet2[2] = vet2[2] + 1
	elif (i == "A"):
		vet2[3] = vet2[3] + 1
	else:
		vet2[4] = vet2[4] + 1
print(max(vet2))
print(vet2)