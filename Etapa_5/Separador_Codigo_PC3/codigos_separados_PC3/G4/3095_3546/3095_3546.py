s = input().upper()
V = 0
E = 0
D = 0
while(s != "X"):
	if(s == "V"):
		V = V + 3
	if(s == "E"):
		E = E + 2
	if(s == "D"):
		D = D + 1
	s = input().upper()
print(V)
print(E)
print(D)