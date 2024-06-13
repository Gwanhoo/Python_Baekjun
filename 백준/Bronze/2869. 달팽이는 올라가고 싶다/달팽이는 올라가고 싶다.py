# A: 하루에 올라갈 수 있는 길이 B: 잠자는 동안 미끄러지는 길이 V: 올라가야하는 길이
A, B, V = map(int, input().split())

# 도착일 x 올라가는 횟수 x 내려가는 횟수 x-1

# Ax - B(x-1) = V
# Ax - Bx + B = V
# Ax - Bx = V - B
# x(A-B) = V - B
# x = (V - B)/(A - B)

x = (V - B)/(A - B)
if x == int(x):
    print(int(x))
else:
    print(int(x)+1)