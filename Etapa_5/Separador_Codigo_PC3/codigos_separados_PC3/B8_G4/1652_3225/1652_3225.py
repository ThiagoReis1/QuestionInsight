from numpy import*
a = input("Digite: ")
ax = a.split(',')
B = 0
PA = 0
PR = 0
A = 0
I = 0

x = zeros(5, dtype = int)

for a in ax:
	if (a == "B"):
		B += 1
	elif (a == "PA"):
		PA += 1
	elif (a == "PR"):
		PR += 1
	elif (a == "A"):
		A += 1
	elif (a == "I"):
		I += 1
x[0] = B
x[1] = PA
x[2] = PR
x[3] = A
x[4] = I

print(max(x))
print(x)