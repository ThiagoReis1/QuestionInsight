nc = int(input("Numero de copias do virus:"))
tr = int(input("taxa de reducao:"))
nci = int(input("Numero de copias introduzidas:"))

soma = nc
i = 0
t = tr/100
r = 1000000

while (soma<=r):
	soma = soma - (soma*t)
	cop = soma + nci
	soma = cop
	i = i+1
print(i)