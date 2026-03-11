T=float(input("Número inicial de tambaquis no viveiro:"))
P=float(input("Número inicial de pacus no viveiro:"))
it=float(input("Taxa anual de crescimento de tambaquis (em %):"))
ip=float(input("Taxa anual de crescimento de pacus (em %):"))
num=float(input("Número máximo de espécies comportadas pelo viveiro:"))

ti= it/100
pi= ip/100
ano = 0
soma = T + P
while(soma <= num):
	T = T+(T * ti)
	P = P+(P * pi)
	soma = T + P
	ano = ano + 1
print(ano)