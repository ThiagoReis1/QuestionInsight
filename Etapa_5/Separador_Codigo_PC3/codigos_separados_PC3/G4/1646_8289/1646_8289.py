from numpy import * 

saq = array(eval(input(":")))
x = 0 

for i in range(size(saq)):
	if saq[i] <= 50 :
		x += 1 

print(x)

j = zeros(x, dtype=int)
k = 0
for i in range(size(saq)):
	if saq[i] <= 50 :
		j[k] += i
		k += 1 
print(j)