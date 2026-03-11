from numpy import*
v = input("v: ").split(",")
y = zeros(5, dtype = int)

for i in range (size(v)):
	if v[i] == "P":
		y[0]+=1
	if v[i] == "C":
		y[1]+=1
	if v[i] == "M":
		y[2]+=1
	if v[i] == "V":
		y[3]+=1
	if v[i] == "A":
		y[4]+=1
print(max(y))
print(y)
