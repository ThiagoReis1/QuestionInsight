from numpy import *

vp = array(eval(input(" ")))
vn = ones(size(vp), dtype = float) #vetor de notas
i = 0

while(i < size(vp)):
	if(size(vn) == size(vp):
		mp = float(sum(vn[i] * vp[i]) / sum(vp))
	i = i + 1
print(round(mp, 2))