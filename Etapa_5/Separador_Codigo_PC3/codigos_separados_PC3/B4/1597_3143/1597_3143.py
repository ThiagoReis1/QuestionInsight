from numpy import*
custo = array(eval(input("custo do produto :")))
if(sum(custo) > 80):
	custo_total = sum(custo) 
else:
	custo_total = sum(custo)
print(round(custo_total,2))