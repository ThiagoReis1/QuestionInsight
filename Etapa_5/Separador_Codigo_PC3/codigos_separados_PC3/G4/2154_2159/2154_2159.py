from numpy import*

# Vetores
P = array(eval(input("Vetor P: ")))
Q = array(eval(input("Vetor Q: ")))

i = 0			# Contadora
conta = 0 	# Acumuladora

# Distância Euclidiana
while (i < size(P)) and (i < size(Q)):
	x = (P[i] - Q[i])**2
	conta = conta + x
	i = i + 1
	
dPQ = conta**0.5
print(round(dPQ,4))

# Similaridade
simPQ = 1/(1 + dPQ)
print(round(simPQ,2))