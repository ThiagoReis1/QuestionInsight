from numpy import*

vt = array(eval(input("manda ver:")))
ax = zeros(size(vt),dtype=int)
for i in range(size(vt)):
		ax[i] = vt[i] * vt[i]
print(ax)