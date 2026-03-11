from numpy import *
vet= array(eval(input()))
tot=0
num=0
for i in range(size(vet)):
	if vet[i] > 15:
		tot= tot + vet[i]
		num= num + 1

if tot> 0:
	media= tot / num
	print(round(media, 2))
else:
	print(0.0)