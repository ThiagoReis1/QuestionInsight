from numpy import*
#alunos reprovados
n = array(eval(input("notas: ")))
t = 0
y = 0
c = 0
while t < size(n):
	if (n[t] < 5):
		c += 1
	t += 1
t = 0
x = zeros(c, dtype=int)
while(t < size(n)):
	if n[t] < 5:
		x[y] = t
		y += 1
	t += 1
print(c)
print(x)