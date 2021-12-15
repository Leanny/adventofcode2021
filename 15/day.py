from queue import PriorityQueue

def generalize(inp):
    def neighbor(x,y):
        if x > 0: yield x-1, y
        if y > 0: yield x, y-1
        if x < l-1: yield x+1, y
        if y < l-1: yield x, y+1

    l = len(inp)
    res = [[10000] * l for _ in range(l)]
    res[0][0] = 0
    pq = PriorityQueue()
    pq.put((0, (0,0)))
    visited = set()
    while not pq.empty():
        _, (x,y) = pq.get()
        visited.add((x,y))
        for x1, y1 in neighbor(x,y):
            if (x1, y1) not in visited:
                dist = inp[y1][x1]
                old_cost = res[y1][x1]
                new_cost = dist + res[y][x]
                if old_cost > new_cost:
                    pq.put((new_cost, (x1, y1)))
                    res[y1][x1] = new_cost

    return res[-1][-1]

def part1(inp):
    return generalize(inp)

def part2(inp):
    l = len(inp)
    return generalize([[(inp[j%l][i%l] + i//l + j//l -1) % 9 + 1 for i in range(l * 5)] for j in range(l * 5)])

def prep_data(inp):
    return [[int(k) for k in i.strip()] for i in inp]

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 40
print(part1(data))
assert part2(data_test) == 315
print(part2(data))