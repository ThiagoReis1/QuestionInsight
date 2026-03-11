a = int(input("qual numero ?"))
b = a // 10000
r = a % 10000
e = r // 100
f = r % 100
c = b ** 3 + e ** 3 + f ** 3
if(c == a):
   mensagem = "X atende a propriedade"
else:
	 mensagem = c
print(mensagem)


