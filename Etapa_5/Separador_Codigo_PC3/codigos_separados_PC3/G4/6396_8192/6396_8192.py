from numpy import*

v = array(eval(input("digite a senha:")))

cont = zeros(size(v), dtype=int)

for i in range(size(v)):
	cont[i] = v[i] * 2
	
print(cont)