from numpy import*

a = input().split(",")
b = zeros(5, dtype= int)

for i in range(size(a)):
	if a[i] == "A":
		b[0] = b[0] + 1
	elif a[i] == "B":
		b[1] = b[1] + 1
	elif a[i] == "C":
		b[2] = b[2] + 1
	elif a[i] == "D":
		b[3]= b[3] + 1
	elif a[i] == "E":
		b[4] = b[4] + 1
print(b)
	
