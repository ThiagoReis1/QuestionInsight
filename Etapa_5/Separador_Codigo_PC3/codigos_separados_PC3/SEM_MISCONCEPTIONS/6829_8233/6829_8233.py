from numpy import*
string=input("letras cada produto:").upper()
i=0
total=0
A=0
L=0
P=0
while i<len(string):
	if string[i]=="A":
		total = total + 19.90
		A = A + 1
	elif string[i] == "L":
		total = total + 3.50
		L = L + 1
	else string[i] == "P":
		total =total + 4.25
print(round(total,2))