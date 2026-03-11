x=int(input("X atende a propriedade:"))
a=x//100*7
b=(x%100*7)//10
c=(x%100*7)%10
soma= a+b+c
print(soma) 
if(soma):
	print("x atende a propriedade")
else:
	print("x nao atende a propriedade")
	