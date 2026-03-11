pergaminhos= int(input())
varinhas= int(input())
crescimento_p= float(input())
crescimento_v= float(input())

total=80000
anos=0
final = pergaminhos*(crescimento_p/100) + varinhas * (crescimento_v/100)

while(final<total):
	final = pergaminhos*(crescimento_p/100) + varinhas * (crescimento_v/100)
	anos=anos+1
   print(anos)
   