from math import*
from numpy import*

v = array(eval(input("Digite um vetor: ")))
v = v.split
tam = size(v)

if v[i] == "B" :
	v[i] = Branco
elif v[i] == "PA":
	v[i] = Pardo
elif v[i] == "PR":
	v[i] = Preto
elif v[i] == "A":
	v[i] = Amarelo
else:
	v[i] = Indígena
	
v_novo = zeros(tam)

for elemento in v:
	if v[i] == Branco:
		B = B + 1
	elif v[i] == Pardo:
		PA = PA + 1
	elif v[i] == Preto:
		P = P + 1
	elif v[i] == Amarelo:
		A = A + 1
	else:
		I = I + 1
	
v_novo = (B,PA,P,A,I)

