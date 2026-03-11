N = int(input("informe o numero total de termos "))
i = 1
j = 3 #variavel do denominador
k = 1 #auxiliar de sinal da operacao
s = 0

while(i <= N):
	s = s + (((-1)*i**3)/(9+j)) * k
	i = i+1 
	j = j + 2
	k = k*(-1)
print(round(s, 8))