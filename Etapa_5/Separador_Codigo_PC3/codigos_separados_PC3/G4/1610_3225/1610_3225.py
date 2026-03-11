from numpy import*
v = input()
conv = v.split(',')
i = 0
while(i < size(conv)):
	conv[i] = int(conv[i])
	i = i + 1
print(sum(conv))