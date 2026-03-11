from numpy import*

v = array(eval(input("digite:")))
cont = 0
for i in range(size(v)):
	n = v[i] / 100
	if (n >= 0.7 and n <= 1.0):
		cont = cont + 1
cnt = zeros(cont, dtype=int) 
c = 0
for i in range(size(v)):
	n = v[i] / 100
	if (n >= 0.7 and n <= 1.0):
		cnt[c] = cnt[c] + i
		c = c + 1
print(cont)
print(cnt)
