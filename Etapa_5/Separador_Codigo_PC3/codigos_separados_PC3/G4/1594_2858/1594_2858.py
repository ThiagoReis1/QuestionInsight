from numpy import*
#from ling.ly import*
j = 1
cont = 0
#w = zeros(3, dtype=int)
n = eval(input("vetor: "))
for i in range(size(n)):
	cont =cont + n[i] * j
	j = j + 1
	
print(cont)