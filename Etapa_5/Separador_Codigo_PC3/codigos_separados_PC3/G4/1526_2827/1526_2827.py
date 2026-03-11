a = int(input("Quantidade inicial de mana da bruxa Sosípatra: "))
b = int(input("Quantidade de mana que ela gasta por dia: "))
c = int(input("Quantidade de mana que ela recupera por noite de sono: "))

soma = (a - b) + c
i = 1

while(soma > 0):
	soma = soma - b + c
	i = i + 1
print(i)