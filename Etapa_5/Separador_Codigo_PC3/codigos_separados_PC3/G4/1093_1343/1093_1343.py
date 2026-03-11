num1=int(input("Insira o numero:"))
num2=num1//100
num3=num1%100
difnum=((num2+num3)**2)
if(num1==difnum):
	print(num1,"atende a propriedade")
else:
	print(difnum)