from numpy import*

mes = array(eval(input("Digite os numeros da mensagem: ")))

cont = zeros(size(mes), dtype=int)

for i in range(size(mes)):
	if(mes[i]==0):
		cont[i] = 9**2
	else:
		cont[i] = (mes[i]-1)**2

print(cont)