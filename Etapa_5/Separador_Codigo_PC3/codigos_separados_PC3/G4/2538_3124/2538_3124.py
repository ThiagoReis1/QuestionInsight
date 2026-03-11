S = float(input())
D = float(input())
M = float(input())
j = float(input())
s = 0
t = 0

if(S>0 and D>0 and M>0 and j>0):
	while(s < S):
		vi = D * j/100
		saldo = saldo + vi
		t = t + 1
		print(round(s,2))		