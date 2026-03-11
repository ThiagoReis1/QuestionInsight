n = int(input("numerotestado"))
u = n%10
d = (n%100-n%10)//10
c = (n%1000-n%100)//100
m = (n%10000-n%1000)//1000
q = (10*d+u)**2+(10*m+c)**2
r = u+10*d+100*c+1000*m
if (q == r):	
	print("atende")
else:	
	print("nao atende")	
print(n)	
    

