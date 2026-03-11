from numpy import*
nf = array(eval(input("digite as notas finais:")))
ap = 0
for i in nf :
	if(i>=5):
		ap = ap + 1
v = zeros(ap,dtype=int)
d = 0
i = 0
for i in range(size(nf)) :
	if(nf[i]>=5):
		v[d]= i
		d = d + 1
print(ap)
print(v)
		