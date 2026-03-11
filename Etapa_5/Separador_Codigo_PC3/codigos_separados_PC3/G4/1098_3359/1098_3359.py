a = float(input('numero fornecido: '))
n1 = a // 1000
n2 =(a % 1000) 

cal = (n1-n2)**4
if (a == cal):
	mens='atende'
else:
	mens='nao atende'
print(a)
print(mens)