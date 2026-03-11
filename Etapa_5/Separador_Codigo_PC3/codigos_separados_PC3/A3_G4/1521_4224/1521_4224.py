num=int(input("capacid"))
qi=int(input("estoque"))
chega=int(input("qi"))
temp=1
i=0


#quantas semanas o navio leva para esvaziar o qi

while(i<qi):
	qi=qi+(chega*temp)
	qf=qi-(num*temp)
	temp=temp+1
	i=i+1
print(temp)