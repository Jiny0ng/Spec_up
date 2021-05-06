import sys

point, line, start = sys.stdin.readline().strip().split(" ")#문자형으로 입력 받았기에 정수형으로 형변환 해야됨
start = int(start)
point = int(point)
map = [[]for i in range(int(line))]

for i in range(int(line)) :
    a,b = sys.stdin.readline().strip().split(" ")
    map[i] = [int(a), int(b)]

map.sort(key = lambda x : (x.count(start), x[0]+ x[1]))
DFS_stack = [start]
DFS_visit = [start]
BFS_que = []
BFS_visit = [start]
def DFS(start) :
    
    map.sort(key = lambda x : (-x.count(start), x[0]+ x[1]))
    for i in map :
        if i[0] == start and DFS_visit.count(i[1])==0:
            DFS_stack.append(i[1])
            DFS_visit.append(i[1])         
            DFS(DFS_stack[-1])
            
        if i[1] == start and DFS_visit.count(i[0])==0 :
            DFS_stack.append(i[0])
            DFS_visit.append(i[0])           
            DFS(DFS_stack[-1])
    DFS_stack.pop()
   
    return
        
def BFS(start,point) :
    BFS_que.append(start)
    while len(BFS_que) > 0:
        start = BFS_que[0]
        map.sort(key = lambda x : (x.count(start), x[0]+ x[1]))
        
        for i in map :
            if i[0] == start and BFS_visit.count(i[1]) == 0:
                BFS_que.append(i[1])
                BFS_visit.append(i[1])
                
            if i[1] == start and BFS_visit.count(i[0]) == 0:
                BFS_que.append(i[0])
                BFS_visit.append(i[0])      
                
        BFS_que.pop(0)
        

DFS(start)
BFS(start,point)

for i in DFS_visit : sys.stdout.write(f"{i} ")
sys.stdout.write("\n")
for i in BFS_visit : sys.stdout.write(f"{i} ") 
