total=int(input())
x=int(input())
y=int(input())
tempo=0

while(total>0):
	total=(total+x)-y
	tempo=tempo+1
	
print(tempo)