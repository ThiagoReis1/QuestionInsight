X= int(input())
s1=X//100
s2=(X%100)//10
s3=(X%100)%10//1

if (s1**3 + s2**3 + s3**3 == X):
	
	print(X, "atende a propriedade")
else:
	print(s1**3 + s2**3 + s3**3)
	