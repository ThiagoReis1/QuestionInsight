from numpy import*
n = array(eval(input("")))
acm = zeros(size(n), dtype=int)

for i in range(size(n)):
	acm[i] = n[i] * 2 
print(acm)