from numpy import*
v = array(eval(input("Passageiros por parada: ")))
soma = 0
i = 0
while(i<len(v)-1):
	soma = soma + v[i]
	i = i + 1
if(soma>75):
	soma = 75 + v[-1]
else:
	soma = soma + v[-1] 
print(int(soma))