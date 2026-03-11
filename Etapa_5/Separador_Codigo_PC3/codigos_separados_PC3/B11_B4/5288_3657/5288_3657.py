i=0
j=0
idade=""
while(idade!=-1):
	if(idade==""):
		idade=int(input("De a idade: "))
		if(idade!= -1):
			i=i+1
			if(idade<18):
				j=j+1
	else:
		idade=int(input("De a idade: "))
		if(idade!= -1):
			i=i+1
			if(idade<18):
				j=j+1
percent=j/i
percent=percent*100
print(i)
print(round(percent,2))