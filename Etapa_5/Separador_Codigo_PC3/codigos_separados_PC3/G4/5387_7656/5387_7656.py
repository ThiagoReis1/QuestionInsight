from numpy import*

s = input("").upper()
i = 0
t = 0
n = len(s)

while(i<n):
	if(s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
		t = t + 45.12
	else:
		t = t + 50.18
	i = i + 1

print(round(t,2))