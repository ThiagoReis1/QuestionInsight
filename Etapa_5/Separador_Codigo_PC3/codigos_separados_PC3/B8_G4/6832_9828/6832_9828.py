from numpy import *
cmp = input("Compras: ").upper()
cm = list(cmp)
c = 0

while c < len(cm):
	if cm[c] == "H":
		cm[c] = 5.4
	elif cm[c] == "C":
		cm[c] = 8.95
	elif cm[c] == "L":
		cm[c] = 4.5
	c+=1

print(sum(cm))