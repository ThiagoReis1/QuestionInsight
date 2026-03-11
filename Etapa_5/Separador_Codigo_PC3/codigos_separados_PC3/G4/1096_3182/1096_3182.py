num=int(input("digite um num"))

n1=num//10000
n2=num%10000//100
n3=num%100

x=n1**3+n2**3+n3**3

if(num==x):
	mensagem= "atende"
	
else:
	mensagem="nao atende"
print(mensagem)
print(num)