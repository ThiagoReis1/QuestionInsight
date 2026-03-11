a= str(input()).lower()
if(a=="aspartato"):
	valor=(4*12.011)+(6*1.00794)+(14.0067)+(4*15.9994)
	print(round(valor,2))
elif(a=="cisteina"):
	soma=(3*12.011)+(7*1.00794)+(14.0067)+(2*15.9994)+(32.066)
	print(round(soma,2))
elif(a=="metionina"):
	total=(5*12.011)+(11*1.00794)+(14.0067)+(2*15.9994)+(32.066)
	print(round(total,2))
else:
	print("Entrada:",a)
	print("Dado Invalido")