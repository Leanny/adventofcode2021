def get_lowpoints(inp):
    res = []
    l = len(inp[0])
    l2 = len(inp)
    for y in range(l2):
        for x in range(l):
            if y == 0:
                if x == 0:
                    if inp[y+1][x] > inp[y][x] < inp[y][x+1]:
                        res.append((y, x))
                elif x == l-1:
                    if inp[y+1][x] > inp[y][x] < inp[y][x-1]:
                        res.append((y, x))
                else:
                    if inp[y][x+1] > inp[y][x] < inp[y][x-1] and inp[y+1][x] > inp[y][x]:
                        res.append((y, x))
            elif y == l2-1:
                if x == 0:
                    if inp[y-1][x] > inp[y][x] < inp[y][x+1]:
                        res.append((y, x))
                elif x == l-1:
                    if inp[y-1][x] > inp[y][x] < inp[y][x-1]:
                        res.append((y, x))
                else:
                    if inp[y][x+1] > inp[y][x] < inp[y][x-1] and inp[y-1][x] > inp[y][x]:
                        res.append((y, x))
            else:
                if x == 0:
                    if inp[y-1][x] > inp[y][x] < inp[y][x+1] and inp[y+1][x] > inp[y][x]:
                        res.append((y, x))
                elif x == l-1:
                    if inp[y-1][x] > inp[y][x] < inp[y][x-1] and inp[y+1][x] > inp[y][x]:
                        res.append((y, x))
                else:
                    if inp[y][x+1] > inp[y][x] < inp[y][x-1] and inp[y-1][x] > inp[y][x] < inp[y+1][x]:
                        res.append((y, x))
    return res
def part1(inp):
    lp = get_lowpoints(inp)

    return sum([inp[y][x] for y,x in lp])+len(lp)

def part2(inp):
    lp = get_lowpoints(inp)
    res = []
    l = len(inp[0])
    l2 = len(inp)
    for y,x in lp:
        queue = [(y,x)]
        visited = set()
        while len(queue) > 0:
            y1, x1, queue = queue[0][0], queue[0][1], queue[1:]
            if (y1, x1) in visited: continue
            visited.add((y1, x1))
            if y1 != 0:
                if inp[y1][x1] < inp[y1-1][x1] and inp[y1-1][x1] != 9:
                    queue.append((y1-1,x1))
            if y1 != l2-1:
                if inp[y1][x1] < inp[y1+1][x1] and inp[y1+1][x1] != 9:
                    queue.append((y1+1,x1))
            if x1 != 0:
                if inp[y1][x1] < inp[y1][x1-1] and inp[y1][x1-1] != 9:
                    queue.append((y1,x1-1))
            if x1 != l-1:
                if inp[y1][x1] < inp[y1][x1+1] and inp[y1][x1+1] != 9:
                    queue.append((y1,x1+1))
        res.append(len(visited))

    res = sorted(res)
    return res[-1] * res[-2] * res[-3]

def prep_data(inp):
    res = [[int(k) for k in i.strip()] for i in inp]
    return res

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 15
print(part1(data))
assert part2(data_test) == 1134
print(part2(data))