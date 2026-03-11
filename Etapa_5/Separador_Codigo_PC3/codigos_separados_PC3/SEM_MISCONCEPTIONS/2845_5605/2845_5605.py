from numpy import*
entrada= array(eval(input("")))
saida=[]
for num in entrada:
	if num == 9:
		saida.append(0)
	else:
		saida.append(num+1)

resultado = "["+" ".join(map(str,saida))+"]"
print(resultado)