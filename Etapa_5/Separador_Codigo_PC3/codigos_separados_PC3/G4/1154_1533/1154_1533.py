n = int(input("P: "))
taxa = float(input(" T: "))
c = int(input("P/S"))

soma = n
i = 0
t = taxa/100
r = 1000000
while(soma <=r):
	soma = soma - (soma*t)
	cop = soma + c
	soma = cop
	i = i+1
print(i)