import sys

count = int(sys.stdin.readline())#sys.sdtin.readine은 가장 빠른 입력 함수 이며 import sys를 해줘야 하고 입력 마지막에 줄넘김이 붙어 strip으로 지워줘야함
map = [sys.stdin.readline().strip() for _ in range(count)]

map = list(set(map))
map.sort(key = lambda x : (len(x), x))#sort의 기본 기능으로 lambda를 이용해 저 기준대로 순서대로 정렬함 만약 1번기준이 같은 경우 2번기준대로 정렬함


for i in map :
    print(i)