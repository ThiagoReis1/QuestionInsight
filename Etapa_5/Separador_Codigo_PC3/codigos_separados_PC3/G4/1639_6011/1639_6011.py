from numpy import*

m = array(eval(input("")))
a = zeros(size(m),dtype=int)
cont = 0
for i in range(size(m)):
	if(m[i]%2==0):
	   a[cont] = i
	   cont = cont + 1
print(cont)
print(a[:cont])
	
