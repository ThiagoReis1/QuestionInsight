from numpy import*
p = float(input("Digite um numero maior que 1: "))
x = array(eval(input("Digite o primeiro vetor: ")))
y = array(eval(input("Digite o segundo vetor: ")))

q = p / (p + 1)

c = zeros(size(x), dtype = float)

for i in range(size(x)):
	c[i] = x[i] + y[i]

soma = 0
for i in range(size(x)):
	soma = soma + abs(c[i]) ** q
	

r = soma ** (1 / q)
print(round(r,3))
