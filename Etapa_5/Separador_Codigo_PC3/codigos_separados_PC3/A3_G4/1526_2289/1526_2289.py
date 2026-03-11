n = int(input())
k = int(input())
q = int(input())
e = 0
s = 0
while k>0:
	k = k*n+q
	s = s + 1

print(s)