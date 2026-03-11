from numpy import* 

a = array(eval(input("digite:")))

d = 0
for i in range(size(a)):
	if a[i] % 2 != 0 :
		d +=1
	i+=1
print(d)

b = zeros(d,dtype=int)
c = 0
for i in range(size(b)):
	if b[i] % 2 != 0:
		print(b)
	i+=1
pri
