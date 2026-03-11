A = input("")
Q = int(input())
Re = int(input())

X = 5
s = 3.50
R = 4

if (A == "L"):
	L = X*Q + R*Re
	print(round(L,2))
else:
	S = s*Q + R*Re
	print(round(S,2))