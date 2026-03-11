from numpy import*
qta = array(eval(input("quant de alunos:")))
ip = 0
# quantidades impares de alunos
for i in qta:
	if (i%2 != 0):
		ip = ip + 1

# valor dos indices
n = zeros(ip,dtype=int)
v = 0
i = 0
for i in range(0,size(qta)):
	if(qta[i]%2 != 0):
		n[v] = i
		v = v +1
	i = i + 1
print(ip)
print(n)