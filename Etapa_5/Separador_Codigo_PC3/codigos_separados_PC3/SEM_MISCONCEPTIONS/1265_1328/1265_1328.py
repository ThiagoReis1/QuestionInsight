from numpy import*
p = float(input(""))
x = eval(input(""))
y = eval(input(""))

q = p/(p-1)

v = zeros(size(x),dtype = float)
for i in range(size(x)):
	v[i]=2x[i]+3y[i]

	soma = 0

for j in v:
	soma+=abs(j)**q

print(round(soma**(i/q),3))