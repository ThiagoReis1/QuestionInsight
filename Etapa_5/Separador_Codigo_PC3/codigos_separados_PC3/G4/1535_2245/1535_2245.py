x = float(input("Digite o numero: "))
k = float(input("Digite o numero: "))

i = 1
j = 0
s = 0
sinal = +1
while(j < k):
	s = s + sinal * (x **i/ i)
	sinal = sinal * -1
	i = i + 2
	j = j + 1
print(round(s,6))