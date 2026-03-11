from numpy import*

a = array(eval(input()))

pt = zeros(size(a), dtype = int)

i = 0

while(i < size(a)):
	if(a[i] == 1):
		pt[i] = pt[i] + 80
	if(a[i] == 2):
		pt[i] = pt[i] + 40
	if(a[i] == 3):
		pt[i] = pt[i] + 20
	if(a[i] == 4):
		pt[i] = pt[i] + 10
	i = i + 1

print(sum(pt))