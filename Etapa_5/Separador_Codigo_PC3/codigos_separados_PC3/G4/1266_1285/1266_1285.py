from numpy import*
p = float(input("Digite maior que 1: "))
x = array(eval(input("Vetor x: ")))
y = array(eval(input("Vetor y: ")))
t = p/(p-1)
vet = 2*x-y
term = 0
for i in range(size(vet)):
	term = term + ((abs(vet[i]))**t)
normaq = term ** (1/t)
print(round(normaq,4))