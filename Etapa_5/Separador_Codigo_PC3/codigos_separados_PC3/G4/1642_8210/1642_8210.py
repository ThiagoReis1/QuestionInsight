from numpy import*
v = array(eval(input("v: ")))
x = 0

for i in range(size(v)):
	if v[i]%5 == 0:
		x = x + 1
print(x)

z = zeros(x, dtype=int)
j = 0
for i in range(size(v)):
	if v[i]%5 == 0:
		z[j] = i
		j=j+1

print(z)