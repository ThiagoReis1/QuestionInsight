from numpy import*
n = input("Digite a nacionalidade: ").upper()
v = n.split(',')
q = zeros(5,dtype=int)

for i in range(size(v)):
	if(v[i] == 'AR'):
		q[0] = q[0] + 1
	if(v[i] == 'BR'):
		q[1] = q[1] + 1
	if(v[i] == 'CL'):
		q[2] = q[2] + 1
	if(v[i] == 'CO'):
		q[3] = q[3] + 1
	if(v[i] == 'UY'):
		q[4] = q[4] + 1
print(max(q))
print(q)
