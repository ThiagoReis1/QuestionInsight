num = int(input())
soma=0
quant5=0
while(num!=-1):
	soma+=1
	if(num==5):
		quant5+=1
	num = int(input())
print(soma)
print(round(100*quant5/soma,2))