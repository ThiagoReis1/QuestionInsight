v=float(input())
l=float(input())
a=float(input())
r=float(input())
 
compra_total = v+l+a

print(round(compra_total,2))

if(compra_total<= r):
   print("Nao ultrapassou")
else:
	print("Ultrapassou")
