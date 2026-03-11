x = float(input())
k = int(input())
nc=0
up=2
sinal=1
cont=1
while(cont<k):
	c = x**up
	nc=nc+c*sinal
	up=up+2
	sinal=-sinal
	cont=cont+1
print(round(1-nc,8))