from numpy import*
v = array(eval(input("CH dos alunos: ")))

apr = 0

for i in range (size(v)):
	if (v[i] <= 70):
		apr = apr + 1

vr = zeros(apr, dtype = int)
j = 0
for i in range (size(v)):
	if (v[i] <= 70):
		vr[j] = i
		j = j + 1

print(apr)
print(vr)




