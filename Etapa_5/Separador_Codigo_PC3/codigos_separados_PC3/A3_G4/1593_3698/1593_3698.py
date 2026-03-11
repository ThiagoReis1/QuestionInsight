from numpy import * 
n = array(eval(input("nota: ")))
t = 0 
i = 0
n2 = zeros(size(n))
while t<size(n):
	n2 = (i+1)*n[i]

m = n2/(i+1)
print(round(m,2))