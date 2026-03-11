from numpy import *
entrada = input("entrada: ").replace("[", "").replace("]", "")
msg = list(map(int, entrada.split(",")))
substitutos = []
for num in msg:
	substituto = (int(num) * 2)
	substitutos.append(substituto)
print('[' + ' '.join(map(str, substitutos)) + ']')
