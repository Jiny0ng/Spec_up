import sys

count = int(sys.stdin.readline().strip())


map = [[]for i in range(count)]

for i in range (count) :
    a,b = sys.stdin.readline().strip().split(" ")
    map[i] = [a,b,i]

map.sort(key = lambda x : (int(x[0]),int(x[2])))

for x in map :
    print(x[0]+" "+x[1])