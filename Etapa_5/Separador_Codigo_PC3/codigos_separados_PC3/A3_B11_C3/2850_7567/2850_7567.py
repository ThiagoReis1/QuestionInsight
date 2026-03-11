from numpy import*
v = array(eval(input("")))
soma = zeros(size(v) , dtype = int)
for i in range(size(v)):
	if(v[i] >= 55):
		soma = zeros(size(v) , dtype = int)
	soma[i] = soma[i] + v[i]
	total = sum(soma)
	if(total >= 55):
		soma = zeros(size(v) , dtype = int)
	total = sum(soma)
print(total)