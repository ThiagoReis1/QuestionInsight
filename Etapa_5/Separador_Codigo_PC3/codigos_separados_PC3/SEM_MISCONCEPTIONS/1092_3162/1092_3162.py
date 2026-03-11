num = int(input("Digite um numero"))
x1 = num//100
x2 = (num%100)//10
x3 = (num%100)%10

xtotal = ((x1)**3+(x2)**3+(x3)**3)

if(xtotal == num):
	mensagem = "atende"
else:
	mensagem = "nao atende"

print(num)
print(mensagem)
