from numpy import*
v = array(eval(input("Qual o vetor de saques?: ")))
va = 0
for i in v:
	if(i % 5 == 0):
		va = va + 1
print(va)	
x = zeros(va, dtype = int)
k = 0
l = 0
while(size(v) > k):
	if(v[k] % 5 == 0):
		x[l] = k
		l = l + 1
	k = k + 1
print(x)	