from numpy import*
vet = array(eval(input()))
print(sum(vet))
a = 0
for i in arange(size(vet)):
	if vet [i] >=5:
		a+=1
print(a)