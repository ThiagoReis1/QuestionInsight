qva = int(input())
qvd = int(input())
t = qva+qvd
if (qva>qvd):
	x = (100*qva)/t
	print("Ambrosio Rutra")
	print(round(x,2))
else:
	x = (100*qvd)/t
	print("Demelza Olecram")
	print(round(x,2))
