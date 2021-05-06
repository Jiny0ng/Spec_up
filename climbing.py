import sys
count = int(sys.stdin.readline())
number = [0] * 10001

for i in range(0,count) :
    number[int(sys.stdin.readline())] += 1
    

for i in range(0,10001) :
    for y in range (0,number[i]) : 
        print(i)
    