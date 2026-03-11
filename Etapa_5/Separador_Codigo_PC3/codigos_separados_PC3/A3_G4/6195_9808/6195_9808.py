num = int(input('digite o numero de bacterias de uma cultura: '))
taxa = float(input('digite a taxa de crescimento: '))

dobro = num*2
i= 0 
hora = 0

while num < dobro:
	num = num + (num * taxa/100)
	hora+=1
i += 1
print (hora)

