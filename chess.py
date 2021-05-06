y,x = input().split()

y = int (y)
x = int (x)

mapping = [0]*y

"""for i in range(0,y) :
    mapping[i] = input()"""
mapping = [list(map(int,input()))]

mapping = list(map(int,mapping))

black = int('B')
white = int('W')

for i in mapping :
    print(i)



row_start = col_start = 0
row_end = col_end = 8 


def change(y,x) :
    if mapping[y][x]== white :
        return 1
    else :
        return 2
def check(y,x) :
    ans = x*y
    z = 0
    row_start = col_start = 0
    row_end = col_end = 8


    while z == 0 :
        count = 0
        temp_map = mapping[:]
        print(f"row_end = {row_end}, col_end = {col_end}")
        for row in range(row_start,row_end) :
            for col in range(col_start,col_end) :
                print(f"y = {row}, x = {col}")
                if row>=row_start and row < row_end-1 :#아래로 확인
                    if temp_map[row][col] == temp_map[row+1][col] :
                        if change(row+1,col) == 1 :
                            temp_map[row+1][col] = black
                        else :
                            temp_map[row+1][col] = white
                       
                        
                if row>row_start and row < row_end :#위로 확인
                    if temp_map[row][col] == temp_map[row-1][col] :
                        if change(row+1,col) == 1 :
                            temp_map[row-1][col] = black
                        else :
                            temp_map[row-1][col] = white
                        
                if col>=col_start and col < col_end-1 :
                    if temp_map[row][col] == temp_map[row][col+1] :#오른쪽 확인
                        if change(row+1,col) == 1 :
                            temp_map[row][col+1] = black
                        else  :
                            temp_map[row][col+1] = white
                        
                if col>col_start and col <col_end :
                    if temp_map[row][col] == temp_map[row][col-1] :#왼쪽 확인
                        if change(row,col-1) == 1 :
                            temp_map[row][col-1] = black
                        else :
                            temp_map[row][col-1] = white
                       

        for o in range(0,y) :
            for u in range(0,x) :
                if mapping[o][u] != temp_map :
                    count +=1
        if count < ans :
            ans = count
        if col_end == x and row_end == y :#끝까지 다 돌았을 경우
            z += 1
            return ans
        if row_end <=y and col_end < x :#전체적으로 오른쪽 한칸 움직임
            col_end += 1
        if row_end < y and col_end == x :#전체적으로 아래로 한칸 움직임
            col_end = 8 
            row_end += 1


last = int(check(y,x) / 8)
print(f"answer = {last}")