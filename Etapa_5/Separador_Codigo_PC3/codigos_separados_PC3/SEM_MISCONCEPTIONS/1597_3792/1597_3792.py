from numpy import*
v = array(eval(input("vetor")))
i = 0
soma = 0
while i < len(v):
	if v[i] > 80:
		 soma = soma + v[i] - 5
         soma = soma + v[i]
	print(round(soma,2))
v = array(eval(input("vetor")))
i = 0
while i < len(v):
                if v[i] > 80:
                               v[i]= (v[i]/100)*95
                i += 1
soma = sum(v)
print(round(soma,2))