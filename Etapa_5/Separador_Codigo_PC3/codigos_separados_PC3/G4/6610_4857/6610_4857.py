# faça seu código aqui!
n = float(input("Digite um numero: "))
ct=1
ac=0
while(ct <= n):
	if(ct%2 == 0):
		ac = ac + ct
	ct = ct +1
print("soma=",ac)
