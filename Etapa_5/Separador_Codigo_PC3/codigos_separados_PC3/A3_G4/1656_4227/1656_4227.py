from numpy import*
p = input("").split(",")
x = zeros(5, dtype=int)
a = 0
b = 0
c = 0
d = 0
e = 0
for i in range(size(p)):
	if (p[i] == "BE"):
		x[0] = x[0] + 1 
	if (p[i] == "ES"):
		x[1] = x[1] + 1
	if (p[i] == "FR"):
		x[2] = x[2] + 1
	if (p[i] == "IT"):
		x[3] = x[3] + 1
	if(p[i] == "PT"):
		x[4] = x[4] + 1 
a = max(x)
print(a)
print(x)
		