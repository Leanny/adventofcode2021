characters = {True: "█", False: " "}

def pprint(inp, maxx, maxy):
    for y in range(maxy):
        l = ""
        for x in range(maxx):
            l += characters[inp[y][x]]
        print(l)

def part1(inp):
    coords, inst = inp
    maxx = max(c[0] for c in coords)+1
    maxy = max(c[1] for c in coords)+1
    res = [[False] * maxx for _ in range(maxy)]
    for x,y in coords:
        res[y][x] = True

    for foldx, coord in inst:
        if foldx:
            for x in range(coord):
                for y in range(0, maxy):
                    res[y][x] |= res[y][-x-1]
            maxx = coord
        else:
            for x in range(0, maxx):
                for y in range(coord):
                    res[y][x] |= res[-y-1][x]
            maxy = coord
        break

    total = 0
    for y in range(maxy):
        for x in range(maxx):
            total += int(res[y][x])

    return total

def part2(inp):
    coords, inst = inp
    maxx = max(c[0] for c in coords)+1
    maxy = max(c[1] for c in coords)+1
    res = [[False] * maxx for _ in range(maxy)]
    for x,y in coords:
        res[y][x] = True

    for foldx, coord in inst:
        if foldx:
            for x in range(coord):
                for y in range(0, maxy):
                    res[y][x] |= res[y][maxx-x-1]
            maxx = coord
        else:
            for x in range(0, maxx):
                for y in range(coord):
                    res[y][x] |= res[maxy-y-1][x]
            maxy = coord

    pprint(res, maxx, maxy)

def prep_data(inp):
    coords = []
    instructions = []
    mode = False
    for line in inp:
        line = line.strip()
        if line:
            if not mode:
                x,y = line.split(",")
                coords.append((int(x), int(y)))
            else:
                line = line[len("fold along "):]
                var, pos = line.split("=")
                instructions.append((var == "x", int(pos)))
        else:
            mode = True
    return coords, instructions

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 17
print(part1(data))
part2(data)