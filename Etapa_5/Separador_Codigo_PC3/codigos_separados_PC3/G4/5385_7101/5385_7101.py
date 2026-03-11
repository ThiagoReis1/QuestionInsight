from math import*
v = input("Codigo textual: ")
i = 0
j = 0
while (i<len(v)):
	if (v[i]=="A" or v[i]=="E" or v[i]=="I" or v[i]=="O" or v[i]=="U"):
		j = j + 35.15
	else:
		j = j + 42.17
	i = i + 1
print(round(j,2))