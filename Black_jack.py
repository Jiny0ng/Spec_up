num = input()
count = 0
min = int(num) - (9*(len(num)))
if min<0 :
    min = 1

def search(x) :
    map = str(x)
    ex = 0
    for i in range(0,len(map)) :
        ex = ex + int(map[i])
    return x + ex
    
for i in range(min,int(num)) :
    
    if search(i) == int(num) :
        print(i)
        count = 1
        break
    
    
if(count!=1) :
    print(0)