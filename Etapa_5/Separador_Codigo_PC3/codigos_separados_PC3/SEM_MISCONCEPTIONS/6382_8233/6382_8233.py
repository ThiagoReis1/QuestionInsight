from numpy import*
v_entrada=array(eval(input("informe o vetor:")))
v_saida=zeros(size(v_entrada), dtype=int)
for i in range(size(v_entrada)):
	if (v_entrada[i]==9):
		v_saida[i]=0
	else:
		v_saida[i]=v_entrada[i]+1
print(v_saida**2)
