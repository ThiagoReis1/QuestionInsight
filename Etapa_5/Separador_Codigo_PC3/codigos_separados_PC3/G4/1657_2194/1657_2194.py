from numpy import *
k = input("").split(',')
j = zeros(5,dtype=int)
for i in k:
	if (i == "AZ"):
		j[0] = j[0] + 1
	if (i == "CA"):
		j[1] = j[1] + 1
	if (i == "FL"):
		j[2] = j[2] + 1
	if (i == "PA"):
		j[3] = j[3] + 1
	if (i == "WI"):
		j[4] = j[4] + 1
print(max(j))
print(j)
	