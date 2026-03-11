a=int(input("numeroA:"))
c1=(a//100)
c2=(a%100)//10
c3=(a%100)%10
x=c1**3
y=c2**3
z=c3**3
c=x+y+z
if(c==a):
	print(a)
	print("atende")
else:
	print(a)
	print("nao atende")