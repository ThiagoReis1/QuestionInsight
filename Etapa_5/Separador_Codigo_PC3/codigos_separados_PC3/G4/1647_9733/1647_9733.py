from numpy import*

vt = array(eval(input("Manda ver:")))
ax = zeros(size(vt),dtype=int)

cont = 0
for i in range(size(vt)):
	if vt[i] >= 70:
		cont = cont + 1
print(cont)

for i in range(size(vt)):
	if vt[i] >= 70:
		ax[i] = vt[i]
		print(ax)