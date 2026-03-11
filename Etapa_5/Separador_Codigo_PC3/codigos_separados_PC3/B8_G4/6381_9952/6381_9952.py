from numpy import*
a = input().split(",")
b = zeros(4, dtype=int)

for i in range(size(a)):
	if a[i] =="C":
		b[0] = b[0] + 1
	elif a[i] == "O":
		b[1]= b[1] + 1
	elif a[i] =="P":
		b[2] = b[2] + 1
	elif a[i] =="E":
		b[3] = b[3] + 1
print(b)
		