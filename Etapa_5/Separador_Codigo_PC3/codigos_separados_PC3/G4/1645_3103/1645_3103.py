from numpy import*
s = array(eval(input("Qual o vetor de saques?: ")))
sa = 0
for i in s:
	if(i >= 2000):
		sa = sa + 1
print(sa)	
x = zeros(sa, dtype = int)
k = 0
l = 0
while(size(s) > k):
	if(s[k] >= 2000):
		x[l] = k
		l = l + 1
	k = k + 1
print(x)	
	