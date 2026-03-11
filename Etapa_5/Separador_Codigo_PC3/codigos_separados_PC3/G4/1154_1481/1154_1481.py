x = int(input("Número de cópias iniciais do vírus HIV no sangue"))
y = int(input("Taxa de redução de vírus (em %)"))
z = int(input("Número de cópias introduzidas a cada semana"))

soma = x 
i = 0
t = y/100
c = 1000000
while(soma <= c):
	soma = soma - (soma * t)
	cop = soma + z
	soma = cop
	i = i + 1

print(i)	
	