from numpy import*
n=input("").upper()
i=0 
count = 0
while i < len(n):
	if n[i] == "C":
		count+=1
	i += 1 
print(count)