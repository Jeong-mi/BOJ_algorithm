n,m = map(int, input().split(' '))

MAX = 1050;
map_arr = [[0] * MAX for _ in range(MAX)]
trace_arr = [[0] * MAX for _ in range(MAX)]

cnt = 1

for i in range(n):
    map_arr[i] = list(map(int, input().split(" ")))

cur_y, cur_x = map(int, input().split(" "))
cur_y -= 1
cur_x -= 1

while True:
    if(cur_y < 0 or cur_y >= n or cur_x < 0 or cur_x >= m):
        print(-1)
        break

    if(trace_arr[cur_y][cur_x] > 0):
        print(cnt - trace_arr[cur_y][cur_x])
        break

    trace_arr[cur_y][cur_x] = cnt
    cnt += 1

    if(map_arr[cur_y][cur_x] == 1):
        cur_y -= 1
    elif map_arr[cur_y][cur_x] == 2:
        cur_x -= 1
    elif map_arr[cur_y][cur_x] == 3:
        cur_x += 1
    else:
        cur_y += 1