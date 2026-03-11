from numpy import*

t = array(eval(input("Digite a temperatura: ")))

i = 0
cont = 0

while(i< size(t)):
	if(t[i] <= -50 or t[i] <= 20):
		cont = cont + 1
	i = i + 1

k = zeros(cont,dtype = float)
i = 0
j = 0

while (i < size(t)):
	if(t[i] <= -50 or t[i] 
		j = j + 1
	i = i + 1

print(k)
