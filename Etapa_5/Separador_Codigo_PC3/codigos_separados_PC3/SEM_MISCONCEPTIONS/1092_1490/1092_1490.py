n=int(input("digite um numero"))
a=n//100
resto=n%100
b=resto//100
restob=n%10
c=restob
eq=(a**3)+(b**3)+(c**3)
if(eq==n):
	mensagem="X tende a propriedade"
else:
	mensagem="eq"
print(mensagem)

	