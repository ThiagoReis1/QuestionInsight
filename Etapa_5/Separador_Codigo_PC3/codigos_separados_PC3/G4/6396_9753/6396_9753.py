from numpy import*

e = array(eval(input()))
s = zeros(size(e) , dtype= int)

for i in range(size(e)):
	s[i] = e[i] * 2
	

print(s)