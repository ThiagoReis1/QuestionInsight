numero1=int(input("qual o numero?"))
numero2=numero1//1000
numero3=numero1%1000

soma=((numero2-numero3)**4)

if(soma == numero1):
	print(numero1,"atende a propriedade")
else:
	print(soma)