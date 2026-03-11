from numpy import*
n = array(eval(input("Quantidade de alunos: ")))
p = 0

for i in range( size(n) ):
	if(n[i] % 2 == 0):
		p = p + 1
print(p) #Quantidade par de alunos


saida = zeros(p, dtype=int)
x = 0
for i in range( size(n)):
	if(n[i] % 2 == 0):
		saida[x] = i
		x = x + 1

print(saida)