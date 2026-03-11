from numpy import*
v = array(eval(input("Notas: ")))
x = size(v)#
cont = zeros(x, dtype = int)#
ap = 0
for i in v:
	if(i >= 5):
		for i in v:
			face = i
			cont[face-1] = cont[face-1] + 1
		ap = ap + 1
		print(vetor)
	print(ap)
	print(cont)