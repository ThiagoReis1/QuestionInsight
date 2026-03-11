s = int(input())

d1 = s // 100000
rd1 = s % 100000
d2 = rd1 // 10000
rd2 = rd1 % 10000
d3 = rd2 // 1000	
rd3 = rd2 % 1000
d4 = rd3 // 100
rd4 = rd3 % 100
d5 = rd4 // 10
rd5 = rd4 % 10
d6 = rd5 // 1

sm1 = d1 + d2 + d3 + d4 + d5 +d6
sm2 = d1 + d3 + d5
if  ( sm1 // sm2 == sm1 / sm2):
	print("nao atende")
else: 
	print("atende")