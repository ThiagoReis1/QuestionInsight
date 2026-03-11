N=int(input())
i=0
S=0
while(i<=N):
	S=S+ ((-i)**3)*((-1)**i)/(2+(2*i +1))
	i=i+1
print(round(S,8))