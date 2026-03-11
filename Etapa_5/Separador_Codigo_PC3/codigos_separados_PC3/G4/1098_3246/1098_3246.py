n = int(input())

print(n)

d1 = n // 100000
rd1 = n % 100000
d2 = rd1 // 10000
rd2 = rd1 % 10000
d3 = rd2 // 1000
rd3 = rd2 % 1000
d4 = rd3 // 100
rd4 = rd3 % 100
d5 = rd4 // 10
rd5 = rd4 % 10
d6 = rd5 // 1

g = (((d1*100) + (d2 *10) + d3) - ((d4*100)+(d5*10)+ d6)) ** 4

if( g == n):
	print("atende")
	
else:
	print("nao atende")