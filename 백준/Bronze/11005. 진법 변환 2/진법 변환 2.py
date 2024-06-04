N, B = map(int, input().split())
ans = '' 

system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N != 0:
    ans += str(system[N % B])
    N //= B
    
print(ans[::-1])