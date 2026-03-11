#Valores iniciais 
x = float(input("Insira um numero real: "))
k = int(input("Insira a quantidade de termos da serie: "))

#Variavel contadora 
n = 0
arctg = 0 #Variavel acumuladora

#Laco de acumulacao 
while (n < k):
	arctg = arctg + ((-1)**n) * x**(2*n+1)/(2*n+1)
	n = n + 1
	
print(round(arctg,6))
	