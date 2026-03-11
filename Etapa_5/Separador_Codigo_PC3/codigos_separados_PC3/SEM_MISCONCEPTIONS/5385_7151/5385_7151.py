from numpy import*

texto=input()

i=0
total=0

while i<len(texto):
	if texto[i] in "AEIOU":
		total=total+35.15
	else:
		total=total+42.17
	i=i+1
	
print(round(total,2))