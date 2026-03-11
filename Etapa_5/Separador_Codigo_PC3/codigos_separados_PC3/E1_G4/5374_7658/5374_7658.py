from numpy import *
n= input(":")
c= 0
i= 0
while i < len(n):
	if n[i].upper() == "A" or n[i].upper()== "E" or n[i].upper()== "I" or n[i].upper()== "O" or n[i].upper()== "U" or n[i].upper() == "a" or n[i].upper() == "e" or n[i].upper() == "i" or n[i].upper() == "o" or n[i].upper()== "u": 
		c= c+ 0.15 
	else:
		c= c+0.17
	i= i+1
print(round(c,2))
	