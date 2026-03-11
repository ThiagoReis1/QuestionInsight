from numpy import*
i = 0
n = input("enes:").upper()
com = len(n)
d = 0
s = 0
I = 0
S = 0

while n[i] == com:
	if n[i] == 'D':
		s = s+2,25
	if n[1] == 'S':
		s = s+4
	if n[i] == 'I':
		s = s+6,90
i = i+1
print(round(s,2))