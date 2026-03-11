from numpy import *

VN = array(eval(input("chances jogadas")))
PT = 0
i = 0

while i < size(VN):
	if VN[i] == 1:
		PT += 10
	if VN[i] == 2:
		PT += 5
	if	VN[i] == 3:
		PT += 10
	if VN[i] == 4:
		PT += 5
	if VN[i] == 5:
		PT += 10
	if VN[i] == 6:
		PT += 5
	i = i+1
print(PT)
