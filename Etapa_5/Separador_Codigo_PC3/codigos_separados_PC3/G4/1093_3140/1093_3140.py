N=int(input())
N1=(N//100)
N2=N%100
M1=(N1**2)
M2=(N2**2)
S=M1+M2
if( N == S):
	print("atende")
	print(N)
else:
	print("nao atende")
	print(N)
