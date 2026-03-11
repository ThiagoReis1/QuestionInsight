fim = int(input("digite o numero da série :"))
i = 1
soma = 0

while i<= fim:
	soma = soma + (-1)**(1+i)*((i**3)/(2+(i*2+1)))
	i = i + 1
print (round(soma,8))