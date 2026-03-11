from numpy import*

atq = array(eval(input()))
i = 0
j = 1 
dano = 0 
while(i < size(atq)):
	dano = dano + (atq[i]*j)
	j = j + 1 
	i = i + 1
print(dano)
	