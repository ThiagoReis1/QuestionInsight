from math import *

n1= input("Nome do equipamento:").lower()
if(((n1<0)or(n1>1000)) or (n1!= "computador")or(n1!= "freezer")or(n1!= "furadeira")or(n1!= "liquidificador"or(n1!= "microondas")or(n1!= "notebook")or(n1!= "televisor")or(n1!="ventilador")):
	print("Entrada invalida")
elif(n1=="computador"):
	p1=n1*12
elif(n1=="freezer"):
	p2=n1*52
elif(n1=="furadeira"):
	p3=n1*1.7
elif(n1=="liquidificador"):
	p4=n1*1.8
elif(n1=="microondas"):
	p5=n1*15
elif(n1=="notebook"):
	p6=n1*2.5
elif(n1=="televisor"):
	p7=n1*15
elif(n1=="ventilador"):
	p8= n1*2.4
soma=(p1+p2+p3+p4+p5+p6+p7+p8)
print(soma, 2)