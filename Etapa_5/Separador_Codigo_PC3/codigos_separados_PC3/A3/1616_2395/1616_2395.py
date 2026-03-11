from numpy import*
m = array(eval(input()))
n = array(eval(input()))
GELO = 2
FOGO = 3
CHOQUE = 4
CONJURACAO = 8
ILUSAO = 10
dm = zeros(size(m), dtype=int)
i = 0
while(i<size(m)):
	dm[i] = dm + m[i]*n[i]
	i = i + 1
print(dm)