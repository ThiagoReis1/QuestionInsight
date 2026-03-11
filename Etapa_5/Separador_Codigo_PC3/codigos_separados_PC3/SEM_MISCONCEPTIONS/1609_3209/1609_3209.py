from numpy import *
s = array("Vetor: ")
c = input("")
i = 0

while (i < len(s)):
	if (s[i] == "l"):
	s=s
	else:
		s = s.replace(s[i],"r")
	i = i + 1
print(s)
