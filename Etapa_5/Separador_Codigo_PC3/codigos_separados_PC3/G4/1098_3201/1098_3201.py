j=int(input( ))

a=j//1000
m=j%100

y=(a-m)**4

print(j)

if y==j:
	print("atende")
else:
	print("nao atende")