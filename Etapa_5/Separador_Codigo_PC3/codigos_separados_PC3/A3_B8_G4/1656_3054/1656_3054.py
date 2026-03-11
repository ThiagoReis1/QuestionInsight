from numpy import*

v = input("ler: ").split(",")
z = zeros(5, dtype = int)
cont = 0
for i in range(len(v)):
	if(v[i] == "BE"):
		z[0] = z[0] + 1
	elif(v[i] == "ES"):
		z[1] = z[1] + 1
	elif(v[i] == "FR"):
		z[2] = z[2] + 1
	elif(v[i] == "IT"):
		z[3] = z[3] + 1
	elif(v[i] == "PT"):
		z[4] = z[4] + 1
print(max(z))
print(z)
	


	