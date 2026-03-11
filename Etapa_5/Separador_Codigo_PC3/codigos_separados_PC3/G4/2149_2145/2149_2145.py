from numpy import*
p1 = array(eval(input("Digite as notas: ")))
p2 = array(eval(input("Digite as notas: ")))
soma = zeros(size(p1), dtype=float)
x = 0
n = 0
for i in range(size(p1)):
	soma[i] = soma[i] + p1[i] + p2[i]
	x = x + 1
	if soma[i] >= 12:
		n = n + 1
print(soma)
print(n)