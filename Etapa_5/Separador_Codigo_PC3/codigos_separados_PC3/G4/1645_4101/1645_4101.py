from numpy import*
#Vetor de Entrada
v = array(eval(input("Saques Efetuados: ")))
#Contador para quantidade de saques acima do limite
s=0
for i in range(size(v)):
	if(v[i]>=2000):
		s += 1
print(s)
#Vetor de Saída
vs = zeros(s, dtype=int)
#Contador para alocar valores do vetor de entrada para o vetor de sáida
t = 0
for i in range(size(v)):
	if(v[i]>=2000):
		vs[t] = i
		t += 1
print(vs)
		