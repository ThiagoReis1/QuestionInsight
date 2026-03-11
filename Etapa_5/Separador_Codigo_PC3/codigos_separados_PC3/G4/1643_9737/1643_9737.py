from numpy import*

cont = 0
vt = array(eval(input()))

for i in range(size(vt)):
	if vt[i] >= 5:
		cont += 1
print(cont)

c = 0
ax = zeros(cont, dtype=int)
for i in range(size(vt)):
	if vt[i]	 >= 5:
		ax[c] = ax[c] + i
	c += 1
print(ax)