from numpy import*

a = array(eval(input()))
s = zeros(size(a),dtype=int)

for i in range(size(a)):
	s[i] = a[i] + 1
	if a[i] == 9:
		s[i] = a[1] - 9
		
print(s)