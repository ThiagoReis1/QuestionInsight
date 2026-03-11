from numpy import*

vt = array(eval(input("vetor:")))
ax = zeros(size(vt),dtype=int)
for i in range(size(vt)):
	ax[i] = vt[i] + 1
	if vt[i] == 9:
		ax[i] = 0
print(ax)
	