num = int(input())

def fiv(n) :   
    if n <= 1 :
        return n
        
    return fiv(n-1) + fiv(n-2)

print(fiv(num))