vl = float(input())
a = vl // 1000
ra = vl % 1000
c = (a-ra) ** 4
if (vl == c):
	mensagem = "atende"
else:
	mensagem = "nao atende"
print(vl)
print(mensagem)