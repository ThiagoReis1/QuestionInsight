n = int(input("informe o numero total de termos "))
i = 1
j = 1 #variavel do denominador
k = 1 #auxiliar de sinal da operacao
s = 0
while(i <= n):
	s = s + ((i**2)/(4+j)) * k
	i = i+1
	j = j+2
	k = k*(-1)
print(round(s, 8))
	