num = int(input())

def star(x,y,max) :
    if max/3==1 :#최소단위 일때
        if x==1 and y == 1 :
            return 0
        else :
            return 1

    if x>(max/3)-1 and x<=(max/3*2)-1 and y>(max/3)-1 and y<=(max/3*2)-1 :
        return 0
    else :
        return star(x%(max/3),y%(max/3),max/3)

for y in range(0,num) :
    print("\n")
    for x in range(0,num) :
        if star(x,y,num) == 0 :
            print("　",end="")
        elif star(x,y,num) == 1 :
            print("■",end="")
        
