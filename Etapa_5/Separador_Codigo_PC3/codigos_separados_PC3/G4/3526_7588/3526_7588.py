num = float(input())
numK = int(input())

i = 1
k = 0

seq = 0

while(k < numK):
	seq += ((num ** i) / i)
	i += 2
	k += 1

print(round(seq, 7))