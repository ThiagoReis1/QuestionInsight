from numpy import*
est = input("estados: ").upper()
vest = est.split(",")
d = zeros(5,dtype=int)


for i in range(size(vest)):
	if(vest[i] == "AM"):
		d[0] = d[0] + 1
	elif(vest[i] == "PE"):
		d[1] = d[1] + 1
	elif(vest[i] == "MG"):
		d[2] = d[2] + 1
	elif(vest[i] == "SP"):
		d[3] = d[3] + 1
	elif(vest[i] == "RS"):
		d[4] = d[4] + 1
print(max(d))
print(d)