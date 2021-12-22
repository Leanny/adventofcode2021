from itertools import product

def generalize(inp):
    # get extreme values
    xvals = sorted({x[0][0] for _, x in inp} | {x[0][1] + 1 for _, x in inp})
    yvals = sorted({y[1][0] for _, y in inp} | {y[1][1] + 1 for _, y in inp})
    zvals = sorted({z[2][0] for _, z in inp} | {z[2][1] + 1 for _, z in inp})

    # creat map idx -> real val
    xd = {v: idx for idx, v in enumerate(xvals)}
    yd = {v: idx for idx, v in enumerate(yvals)}
    zd = {v: idx for idx, v in enumerate(zvals)}

    # do the task with idx vals instead of real values
    turned_on = set()
    for cube in inp:
        state, ((xmi, xma), (ymi, yma), (zmi, zma)) = cube
        if xmi < xma and ymi < yma and zmi < zma:
            for vec in product(range(xd[xmi], xd[xma+1]), range(yd[ymi], yd[yma+1]), range(zd[zmi], zd[zma+1])):
                if state:
                    turned_on.add(vec)
                else:
                    turned_on.discard(vec)

    # get sum of product from each cube
    return sum((xvals[x+1] - xvals[x]) * (yvals[y+1] - yvals[y]) * (zvals[z+1] - zvals[z]) for x, y, z in turned_on)

def part1(inp):
    return generalize([(b, [[max(-50, min(50, mi)), max(-50, min(50, ma))] for mi, ma in l]) for b, l in inp])

def part2(inp):
    return generalize(inp)

def prep_data(inp):
    data = []
    for line in inp:
        l = line.strip().split(" ")
        parts = l[1].split(",")
        coords = [list(map(int, p[2:].split(".."))) for p in parts]
        data.append(("on" in l[0], coords))
    return data

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 474140
print(part1(data))
assert part2(data_test) == 2758514936282235
print(part2(data))
