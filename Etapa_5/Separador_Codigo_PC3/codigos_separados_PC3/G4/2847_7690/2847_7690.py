from  numpy import*
a = array(eval(input()))
b = zeros(size(a),dtype = int)
for i in range(size(a)):
	b[i] = a[i]**2
print(b)