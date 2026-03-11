from numpy import*
v = array(eval(input("Insira o tipo de anel:")))
c = size(v)
t = 0
v0 = zeros(c, dtype=int)			 
while t < c:
	if v[t]==1:
		v0[t]=80
	elif v[t]==2:
		v0[t]=40
	elif v[t]==3:
		v0[t]=20
	t = t + 1
print(sum(v0))


	