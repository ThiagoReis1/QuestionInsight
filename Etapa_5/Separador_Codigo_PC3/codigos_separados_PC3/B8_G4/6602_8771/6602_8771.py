# faça seu código aqui!
n=int(input())
l=0
c=0
p=0
cont=0

while cont<n:
	x=input().lower()
	cont=cont+1
	if x=='l':
		l=l+1
	elif x=='c':
		c=c+1
	elif x=='p':
		p=p+1

print('L=',l)
print('C=',c)
print('P=',p)