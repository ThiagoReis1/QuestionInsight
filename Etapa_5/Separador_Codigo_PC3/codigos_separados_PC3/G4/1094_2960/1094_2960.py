a = input("")

a0 = int(a[0])
a1 = int(a[1])
a2 = int(a[2])
a3 = int(a[3])
a4 = int(a[4])
a5 = int(a[5])

n1 = (a0*100)+(a1*10)+a2
n2 = (a3*100)+(a4*10)+a5

b = (n1+n2)**2
c = int(a)
if(b==c):
	print("atende")
else:
	print("nao atende")
	
print(a)
	