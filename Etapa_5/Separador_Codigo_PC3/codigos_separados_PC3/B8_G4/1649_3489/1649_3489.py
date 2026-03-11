from numpy import*

a = input("insira a string: ").split(',')

b = zeros(5, dtype=int)

for i in range(len(a)) :
	if (a[i] == "P") :
		b[0] = b[0] + 1
	elif (a[i] == "C") :
		b[1] = b[1] + 1
	elif (a[i] == "M") :
		b[2] = b[2] + 1
	elif (a[i] == "V") :
		b[3] = b[3] + 1
	elif (a[i] == "A") :
		b[4] = b[4] + 1
print(max(b))
print(b)