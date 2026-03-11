from numpy import*
var = array(eval(input("a: ")))
val = zeros(size(var),dtype = int)

for i in range(size(var)):
	if var[i] != 0:
		val[i] = (var[i] - 1) ** 3
	else:
		val[i] = 9 ** 3
print(val)