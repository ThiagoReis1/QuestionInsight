from numpy import*
a = input(" ")
i = 0
s = 0

while(i<len(a)):
	if(a[i] == "A" or a[i]=="E" or a[i]=="I" or a[i]== "O" or a[i]== "U" or a[i]== "a" or a[i] == "e" or a[i] == "i" or  a[i] == "o" or a[i] == "u"):
		s = s + 35.15
	else:
		s = s + 42.17
	i = i + 1

print(round(s,2))
