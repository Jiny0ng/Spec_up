import sys

count = int(sys.stdin.readline())
map = [[]for i in range(count)]#1줄 for문의 기능으로 func for X in list 하면 for 문을 돌면서  func를 실행함

for i in range(0,count) :
    a,b = sys.stdin.readline().split(" ")#a,b를 동시에 입력 받아서 split안에 있는걸 기준으로 나눠서 a와b에 각각 저장함 
    map[i] = [int(a),int(b)]
map.sort()
map.sort(key = lambda x : (x[0], x[1]))

for i in map :
    print(f"{i[0]} {i[1]}")A