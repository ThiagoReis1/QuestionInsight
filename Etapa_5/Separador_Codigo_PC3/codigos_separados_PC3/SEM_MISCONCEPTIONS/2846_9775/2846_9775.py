from numpy import *
code = array(eval(input()))
ncode = zeros(size(code), dtype = int)

for i in range(size(code)):
	ncode[i] = code[i]*2
print(ncode)