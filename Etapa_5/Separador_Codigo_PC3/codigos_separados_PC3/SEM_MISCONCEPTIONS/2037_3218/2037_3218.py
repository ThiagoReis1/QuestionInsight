idade=int(input())
x=0

if(idade>=-1):
	while(idade!=-1):
		if(idade<18):
			x=x+1
		else:
			x=x+0
		idade=int(input())
	print(x)