from numpy import*

comp = input('').upper()

i = 0
acu = 0

a= 19.90
l=3.50
p =4.25

while i<len(comp):
	if comp[i] == "A":
		acu +=a
	elif comp[i] == "L":
		acu +=l
	else:
		acu+=p
	i+=1
	
print(round(acu,2))