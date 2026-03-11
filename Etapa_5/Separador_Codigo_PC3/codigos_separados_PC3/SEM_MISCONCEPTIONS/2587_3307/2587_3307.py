from numpy import*

vel = array(eval(input('Velocidades: ')))

limite = vel[0]
limax = limite + limite * 0.50
q = 0

for i in range(size(vel)):
	if vel[i] > limax:
		print(i)
		q+=1
print(q)