from numpy import*
vs = array(eval(input()))
vr = zeros(size(vs), dtype = int)

for i in range(size(vs)):
	if vs[i] != 0:
		vr[i] = vs[i] - 1
	else:
		vr[i] = 9
		
print(vr)
		




