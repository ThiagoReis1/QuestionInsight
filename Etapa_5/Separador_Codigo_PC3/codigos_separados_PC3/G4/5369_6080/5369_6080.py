from numpy import*
cpf = array(eval(input("cpf: ")))
v = array([9,8,7,6,5,4,3,2,1])
i = 0
t = 0
while i < size(cpf):
	t = t+ cpf[i]*v[i]
	i = i + 1
print(t%11)
