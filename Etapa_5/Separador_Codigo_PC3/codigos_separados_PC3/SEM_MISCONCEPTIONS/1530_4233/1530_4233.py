limite = 80000
q = int(input("Digite um numero: "))
Q = int(input("Digite um numero: "))
per_q = float(input("Digite um numero: "))/100
per_Q = float(input("Digite um numero: "))/100
soma = q + Q

anos = 0 

while(soma<limite) and (soma>0):
	q = ((per_q*q)+q)
	Q = ((per_Q*Q)+Q)
	anos = anos + 1
	soma = q + Q

print(anos)