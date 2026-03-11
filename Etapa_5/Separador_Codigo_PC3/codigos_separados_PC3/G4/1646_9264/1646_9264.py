from numpy import*

v = array(eval(input("Digite o valor do saque: ")))
x = 0 

for i in range(size(v)):
	if v[i] <= 50:
		x +=1
a = zeros(x, dtype = int)
s = 0
for i in range(size(v)):
	if v[i] <= 50:
		a[s] = i
		s = s + 1
print(x)
print(a)
		