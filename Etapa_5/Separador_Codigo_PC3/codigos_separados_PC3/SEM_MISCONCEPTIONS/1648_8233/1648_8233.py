from numpy import*
v_entrada=array(eval(input("informe notas:")))
var=0
for i in range(size(v_entrada)):
	if (v_entrada[i]<70):
		var=var+1
		
print(var)

v_saida=zeros(var,dtype=int)
cont=0
for i in range(size(v_entrada)):
	if (v_entrada[i]<70):
		v_saida[cont]=i
		cont=cont+1
print(v_saida)