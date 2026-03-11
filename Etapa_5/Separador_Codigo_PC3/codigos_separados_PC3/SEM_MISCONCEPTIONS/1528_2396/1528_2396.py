dano=int(input())
total=int(input())
recu=int(input())
rodada=0
while(total>0):
	total=total+recu-dano*5
	rodada=rodada+1
print(rodada)