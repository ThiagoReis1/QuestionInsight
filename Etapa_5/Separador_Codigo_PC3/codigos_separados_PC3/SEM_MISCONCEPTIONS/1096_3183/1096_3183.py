senha = int(input("digite um valor "))

a = (senha//10000)
b =(senha%10000)//100
c=(senha%10000)%100

num= (a**3 + b**3+ c**3)
if(num==senha):
	mensagem = "atende"
else:
	mensagem = "nao atende"

print(mensagem)
print(senha)