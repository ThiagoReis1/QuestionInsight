from numpy import*
s = input().upper()
i = 0
r = 0
while i< len(s):
	if s[i] == "C":
		r = r + 10.50
	if s[i] == "E":
		r = r + 8.75
	if s[i] == "P":
		r = r + 17.90
	i +=1


print(round(r,2))