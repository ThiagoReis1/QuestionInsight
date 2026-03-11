from numpy import *
st = str(input()).split(",")
contador = zeros(4, dtype,int)

for i in range(0,4):
	if st == "A":
		contador[0] =+ 1
	elif st == "P":
		contador[1] + 1
	elif st == "D":
		contador[2] += 1
	elif st == "M":
		contador[3].append(+[1])
	
print(contador)