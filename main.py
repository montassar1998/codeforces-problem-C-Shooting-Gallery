
n = int(input())
ts = sorted((list(map(float,input().strip().split())) for _ in range(n)), key=lambda x:x[2])
d = [0]*n
ans = 0
for i in range(n):
    d[i] = ts[i][3]
    for j in range(i):
        if (ts[i][0]-ts[j][0])**2 + (ts[i][1]-ts[j][1])**2 <= (ts[i][2]-ts[j][2])**2:
            d[i] = max(d[i], d[j]+ts[i][3])
    ans = max(ans, d[i])
print('%.9f'%ans)
