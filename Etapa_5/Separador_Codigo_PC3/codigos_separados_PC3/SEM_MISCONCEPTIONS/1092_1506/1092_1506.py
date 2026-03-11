num=int(input("digite um numero de tres algarismos:"))
n1=num//100
reston1=num%100
n2=reston1//10
reston2=reston1%10
n3=reston2//1
if(num==(n1)**3+(n2)**3+(n3)**3):
	print(num,"atende a propriedade")
else:
	print(n1**3+n2**3+n3**3)