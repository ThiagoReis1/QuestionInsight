import numpy as np
ent = input().split(',')
br = pa = pr = a = i = 0
sai = np.zeros(5,dtype=int)
for i in ent:
	if i == "B":
		sai[0] = sai[0] + 1
	if i == "PA":
		sai[1] = sai[1] + 1
	if i == "PR":
		sai[2] = sai[2] + 1
	if i == "A":
		sai[3] = sai[3] + 1
	if i == "I":
		sai[4] = sai[4] + 1
print(max(sai))
print(sai)
