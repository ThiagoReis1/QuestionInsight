# gabriel siza  de oliveira brandão - 21601146
# av.4

n = int(input("copias iniciais"))
taxa = float(input("taxa"))
c = int(input("copias per week"))

soma = n 
i = 0
t = taxa/100
r = 1000000

while (soma <= r):
	soma = soma - (soma * t)
	copias = soma + c
	soma = copias
	i = i + 1
	
print(i)