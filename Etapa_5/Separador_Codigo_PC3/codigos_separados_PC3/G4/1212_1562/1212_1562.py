from numpy import*

p = array(eval(input("Digite os pesos dos levantamentos:")))

i = 0
cont = 0
k = 307

while (i < size(p)):
	if(p[i]< k):
		cont = cont + 1
	i = i + 1
print(k)
print(cont)
