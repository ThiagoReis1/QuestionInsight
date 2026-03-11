from numpy import*

n = array(eval(input("Digite a Senha: ")))
sn = zeros(size(n), dtype=int)

for i in range(size(n)):
	if n[i]==0:
		sn[i]=9**2
	else:
		sn[i]=(n[i]-1)**2
print(sn)