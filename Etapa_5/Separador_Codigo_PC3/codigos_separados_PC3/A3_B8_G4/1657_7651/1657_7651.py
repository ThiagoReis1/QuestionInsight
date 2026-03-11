from numpy import*
v = input().upper().split(',')
l = 0
l1 = 0
l2 = 0
l3 = 0
l4 = 0
l5 = 0
v1 = zeros(5, dtype=int)
for i in range(0, size(v)):
	if (v[i] == "AZ"):
		l += 1
		v1[0]= v1[0]+1
	elif (v[i] == "CA"):
		l1 += 1
		v1[1]= v1[1]+1
	elif (v[i] == "FL"):
		l2 += 1
		v1[2]= v1[2]+1
	elif (v[i] == "PA"):
		l3 += 1
		v1[3]= v1[3]+1
	elif (v[i] == "WI"):
		l4 += 1
		v1[4]= v1[4]+1
print (max(v1))
print(v1)