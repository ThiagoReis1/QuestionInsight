n=int(input("numero fornecido:"))

a= n//100
b=(n//10)%10
c= n%10
x=(a**3 + b**3 + c**3)
if(n == x):
   msg = "atende"
else:
   msg = "nao atende"
	
print(n)	
print(msg)
	