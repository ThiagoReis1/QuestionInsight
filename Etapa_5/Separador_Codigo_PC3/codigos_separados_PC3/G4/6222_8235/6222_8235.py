X = int(input("num: "))
Y = int(input("num: "))
S = 0
while (X <= Y):
	if (X%2  ==  0):
		S = S + X
	X = X + 1
print(S)