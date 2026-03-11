from numpy import*

se=([10.5,8.75,17.90])

s = input("secao: ").upper()

i=0
c=0

while i<len(s):
	if s[i] == "C":
		c = c + se[0]
	elif s[i] == "E":
		c = c + se[1]
	elif s[i] == "P":
		c = c + se[2]
	i = i + 1
	
print(round(c,2))