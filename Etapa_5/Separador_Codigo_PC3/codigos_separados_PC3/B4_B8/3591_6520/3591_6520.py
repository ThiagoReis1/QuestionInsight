from numpy import*

dados=array(eval(input("dados: ")))

d=0
i=0

while i < size(dados):
	if dados[i] == 1:
		d=d+10
	elif dados[i] == 2:
		d=d+5
	elif dados[i] == 3:
		d=d+10
	elif dados[i] == 4:
		d=d+5
	elif dados[i] == 5:
		d=d+10
	elif dados[i] == 6:
		d=d + 5
i=i+1
print(d)
print(i)