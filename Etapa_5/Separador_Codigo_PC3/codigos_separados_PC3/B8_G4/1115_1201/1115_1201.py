s=float(input())
c=int(input())
print("Entradas: R$ ",s,"e codigo", c)
if(c==101):
	r=s*0.008
	d=s+r
elif(c==102):
	r=s*0.0065
	d=s+r
elif(c==103):
	r=s*0.006
	d=s+r
elif(c==104):
	r=s*0.0055
	d=s+r
if(c==101)or(c==102)or(c==103)or(c==104):
	print("Novo salario: R$",d)
else:
	print("Dado invalido")
