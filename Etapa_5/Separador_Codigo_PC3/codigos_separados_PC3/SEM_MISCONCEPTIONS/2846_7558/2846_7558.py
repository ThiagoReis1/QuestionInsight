from numpy import*

vector1 = array(eval(input()))
vector2 = zeros(size(vector1),dtype = int)

for i in range(size(vector1)):
	vector2[i] = vector1[i]*2
print(vector2)