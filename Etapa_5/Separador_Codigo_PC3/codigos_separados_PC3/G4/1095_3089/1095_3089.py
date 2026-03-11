from math import*
n=int(input("qual o numero: "))
d1= n//10000000
d2= (n// 1000000)% 10
d3=(n//100000)%10
d4= (n//10000)%10
d5=(n//1000)%10
d6=(n//100)%10
d7=(n//10)%10
d8= n%10
c=((d1*1000+d2*100+d3*10+d4*1)+(d5*1000+d6*100+d7*10+d8*1))**2
if (n==c):
   mensagem= "atende"
else:
	mensagem= "nao atende"
print(n)
print(mensagem)

