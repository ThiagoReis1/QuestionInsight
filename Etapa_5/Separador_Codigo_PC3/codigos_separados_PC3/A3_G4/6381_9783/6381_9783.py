from numpy import*
fgh = input(": ").upper().split(',')
mn =array([0,0,0,0])
gffg=0
for i in range (size(fgh)):
	if fgh[i] =="C":
		mn[0] = mn[0] +1
	if fgh[i] == "O":
		mn[1]= mn[1]+1
	if fgh[i] == "P":
		mn[2] = mn[2] + 1
	if fgh[i] == "E":
		mn[3] = mn[3] +1
print(mn)
