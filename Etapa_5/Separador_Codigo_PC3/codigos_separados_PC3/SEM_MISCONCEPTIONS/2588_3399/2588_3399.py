from numpy import*
v = array(eval(input("vetor velocidade: ")))

cont = 0

conta = (v[0] * 20/100) + v[0] # 20%
conta1 =(v[0] * 50/100) + v[0] # 50%

for i in range(size(v)):
	if(v[i] > conta and v[i] < conta1):
		cont = cont + 1
		print(i)
print(cont)
