from numpy import*

vc = input().upper().split(',')
ct = zeros(4, dtype=int)

for vc in vc :
	if vc=="O":
		ct[0]+=1
	elif vc=="D":
		ct[1]+=1
	elif vc=="N":
		ct[2]+=1
	elif vc=="C":
		ct[3]+=1
		
print(ct)