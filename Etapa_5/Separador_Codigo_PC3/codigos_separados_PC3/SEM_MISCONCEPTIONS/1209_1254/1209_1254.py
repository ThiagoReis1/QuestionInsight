from numpy import*

v1 = array(eval(input("Digite o valor da entrada: ")))
record = 74.08

i = 0
count = 0
while(i < size(v1)):
	if(v1[i] == record):
		count = count +1
	i = i + 1
else:
		print(record)
i = 0
count = 0
while(i < size(v1)):
	if(v1[i] > record):
		count = count + 1
	i = i+1	
print(count)