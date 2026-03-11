from numpy import*

nac = input("Nacionalidade: ").lower()
nac = nac.split(',')

z = zeros(5,dtype=int)

for i in nac:
	if(i == "ar"):
		z[0] = z[0] + 1
	elif(i == "br"):
		z[1] = z[1] + 1
	elif(i == "cl"):
		z[2] = z[2] + 1
	elif(i == "co"):
		z[3] = z[3] + 1
	elif(i == "uy"):
		z[4] = z[4] + 1
	
print(max(z))
print(z)