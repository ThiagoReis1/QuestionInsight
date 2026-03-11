x= int(input("digite um numero:"))
A= x // 100
B = x % 100
t= (A)**2 + (B)**2
if(t == x):
	print("atende") 
else:
	print("nao atende")
print(x)