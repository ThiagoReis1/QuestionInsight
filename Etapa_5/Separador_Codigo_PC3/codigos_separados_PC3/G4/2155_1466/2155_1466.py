from numpy import *
a=array(eval(input()))
b=array(eval(input()))
c=zeros(size(a))
for i in range(size(a)):
	c[i]=round(a[i]/(b[i])**2,2)
gordo=c.max()
if(gordo>40):
	s="OBESIDADE MORBIDA"
elif(gordo>=35 and gordo<=39.99):
	s="OBESIDADE SEVERA"
elif(gordo>=30 and gordo<=34.99):
	s="OBESIDADE"
elif(gordo>=25 and gordo<=29.99):
	s="ACIMA DO PESO"
elif(gordo>=18.5 and gordo<=24.99):
	s="PESO NORMAL"
elif(gordo>=17 and gordo<=18.49):
	s="ABAIXO DO PESO"
else:
	s="MUITO ABAIXO DO PESO"
print(c)
print("O MAIOR IMC DA TURMA EH:", gordo, s)