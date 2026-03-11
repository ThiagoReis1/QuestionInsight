from numpy import*
v = array(eval(input("v: ")))

impar = 0
for i in range(size(v)):
	if(v[i]%2!=0):
		impar = impar + 1
		i = i + 1
	else:
		i = i + 1
result = zeros(impar,dtype=int)
k = 0
while impar > k:
	for j in range(size(v)):
		if(v[j]%2!=0): 
			j = j + 1
			k = k + 1
			result[j] = result
print(size(result))
print(result)