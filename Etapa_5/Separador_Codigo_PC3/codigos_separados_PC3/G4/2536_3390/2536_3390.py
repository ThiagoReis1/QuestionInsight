c= float(input())
di= float(input())
mf= float(input())
tj= float(input())
tj= tj/100
i=0
soma= di
soma= round(soma,2)

if (c>0) and (di>0) and (mf>0) and (tj>0):
	while (soma < c):
		acum= (soma + mf) * tj
		acum= round(acum,2)
		soma= soma + mf + acum
		soma= round(soma,2)
		i= i+1
	print(i)
else:
	print("Dados incorretos")
		
		