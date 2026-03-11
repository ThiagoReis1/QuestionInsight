from numpy import*
t = array(eval(input("Digitar vetor: ")))

i = 0
qtd = 0
while(i < size(t)):
	if(t[i] <= 40):
		qtd = qtd + 1
	i = i + 1
v = array(zeros((qtd), dtype = float))
i = 0
n = 0
while(i < size(t)):
	if(t[i] <= 40):
		v[n] = t[i]
		n = n + 1
	i = i + 1
print(v)
