from numpy import*
v = array(eval(input('Digite um vetor:')))
t = 0 #total
for i in v:
	if i % 3 == 0:
		t += 1
print(t)
s = zeros(t, dtype=int)
j = 0
for k in range(size(v)):
	if v[k] %3 ==0:
		s[j] += k
		j += 1
print(s)