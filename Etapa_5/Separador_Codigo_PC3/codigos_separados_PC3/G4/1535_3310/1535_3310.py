#valor real = x
#
#k = quantidade de termos da serie

x = float(input("Digite o valor do numero real: "))
k = int(input("Digite o valor do numero inteiro: "))

s = 0
i = 0

while(i < k):
	s = s + ((-1)**i)*(x**(2*i+1))/(2*i+1)
	i = i + 1
print(round(s,6))





