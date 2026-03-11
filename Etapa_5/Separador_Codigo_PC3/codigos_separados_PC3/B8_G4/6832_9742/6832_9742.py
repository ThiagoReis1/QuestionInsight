from numpy import *

n = input("N: ").upper()
i = 0 
s = 0 

while i<len(n):
	if n[i]=="H":
		s = s + 5.40
	elif n[i]=="C":
		s = s + 8.95
	elif n[i]=="L":
		s = s + 4.50
	i = i  + 1
	
print(round(s,2))
