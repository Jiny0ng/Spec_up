num = int(input("정수를 입력하세요(0<= N <= 0) :"))
ans = 1
for i in range(num,0,-1) :
    ans = i*ans

print(f"{ans}!")