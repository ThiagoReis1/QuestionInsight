num=int(input("qual o numero?"))
pi=num//100
ri=num%100
pd=ri//10
rd=ri%10
form = pi**3 + pd**3 + rd**3
if(form == num):
	print(num)
	print("atende")
else:
	print(num)
	print("nao atende")