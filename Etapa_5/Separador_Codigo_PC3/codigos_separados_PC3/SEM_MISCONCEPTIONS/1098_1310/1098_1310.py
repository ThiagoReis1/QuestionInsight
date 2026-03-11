e=int(input("digite um número de seis digitos:"))
resto1=e%10
nmult1=e-resto1
nnum1=nmult1//10
resto2=nnum1%10
nmult2=nnum1-resto2
nnum2=nmult2//10
resto3=nnum2%10
nmult3=nnum2-resto3
nnum3=nmult3//10
m=e%1000
a=(nnum3-m)**4
if a==e:
	print(e, "atende a propriedade")
else:
	print(int(a))