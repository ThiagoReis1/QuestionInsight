al= float(input("altura do leao:"))
tl= float( input("taxa de crescimento do leao:"))
am = 1.4
tm = 0.06
ano = 0

while am < al:
	am= tm + am
	al= tl + al
	ano = ano + 1
print(ano)