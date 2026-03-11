from numpy import*
seq = input("digite: ")
c = zeros(4, dtype=int)

O = 0
D = 0
N = 0
C = 0

for i in range(len(seq)):
	if(seq[i] == "O"):
		c[0] += 1
	elif(seq[i] == "D"):
		c[1] += 1
	elif(seq[i] == "N"):
		c[2] += 1
	elif(seq[i] == "C"):
		c[3] += 1
print(c)