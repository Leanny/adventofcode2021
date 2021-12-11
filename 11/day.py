def step(inp_clone):
    l = len(inp_clone)
    def check_and_add(x1, y1):
        if (x1, y1) not in changed:
            inp_clone[x1][y1] += 1
            if inp_clone[x1][y1] > 9:
                to_change.add((x1, y1))
    to_change = set()
    for x in range(l):
        for y in range(l):
            inp_clone[x][y] += 1
            if inp_clone[x][y] > 9:
                to_change.add((x,y))

    changed = set()
    while len(to_change) > 0:
        x, y = to_change.pop()
        if (x,y) in changed: continue
        changed.add((x,y))
        if y != 0:
            check_and_add(x, y-1)
        if y != l-1:
            check_and_add(x, y+1)
        if x != 0:
            check_and_add(x-1, y)
        if x != l-1:
            check_and_add(x+1, y)
        if y != 0 and x != 0:
            check_and_add(x-1, y-1)
        if y != 0 and x != l-1:
            check_and_add(x+1, y-1)
        if y != l-1 and x != 0:
            check_and_add(x-1, y+1)
        if y != l-1 and x != l-1:
            check_and_add(x+1, y+1)

    for x,y in changed:
        inp_clone[x][y] = 0

    return len(changed)

def part1(inp):
    inp_clone = [list(x) for x in inp]
    return sum(step(inp_clone) for _ in range(100))


def part2(inp):
    i = 1
    inp_clone = [list(x) for x in inp]
    while step(inp_clone) != 100:
        i += 1
    return i

def prep_data(inp):
    res = [list(map(int, i.strip())) for i in inp]
    return res

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 1656
print(part1(data))
assert part2(data_test) == 195
print(part2(data))