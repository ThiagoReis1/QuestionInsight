vs= float(input())
vi= float(input())
dm= float(input())
tj= float(input())
m=0

if(vs>0 and vi>0 and dm>0 and tj>0):
	while(vi<vs):
		vi= vi + dm + dm * tj
		m= m + 1
	print(m)
else:
	print("Dados incorretos")