from numpy import *


p = input().upper().split(",")
cm = zeros(4,dtype=int)
for i in p:
	if i == "O":
		cm[0] = cm[0] + 1
	elif i == "D":
		cm[1] = cm[1] + 1
	elif i == "N":
		cm[2]= cm[2] + 1
	elif i == "C":
		cm[3]= cm[3] + 1
print(cm)
		

