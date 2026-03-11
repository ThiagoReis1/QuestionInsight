from numpy import *

sim = input("Digite: ").upper().split(",")
count = zeros(4,dtype=int)
for i in range(size(sim)):
	if (sim[i] == "A"):
		count[0] = count[0] + 1
	if (sim[i] == 'P'):
		count[1] = count[1] + 1
	if (sim[i] == 'D'):
		count[2] = count[2] + 1
	if (sim[i] == 'M'):
		count[3] = count[3] + 1
	
print(count)