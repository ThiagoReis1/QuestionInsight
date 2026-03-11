from numpy import*
count = zeros(5,dtype=int)
v = input().upper().split(',')
for i in v:
	if v[i] == "P":
		count[0]+=1
	elif v[i] == "C":
		count[1] +=1
	elif v[i] == "R":
		count[2]+=1
	elif v[i]=="L":
		count[3]+=1
	elif v[i] == 'B':
		count[4]+=1
print(max(count))
print (count)