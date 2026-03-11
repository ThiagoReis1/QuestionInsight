h = int(input())
v = int(input())
trans = int(input())
Y = int(input())

t = 1
soma = v 
while(h > soma ): 
	rendv = soma*trans - Y
	soma = soma + rendv
	t = t + 1
print(t)