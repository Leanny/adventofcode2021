from itertools import combinations

def get_correct_maps(inp):
    def transform(c, idx):
        if idx == 0: return (c[0], c[1], c[2])
        if idx == 1: return (c[0], -c[1], -c[2])
        if idx == 2: return (c[1], c[0], -c[2])
        if idx == 3: return (c[1], -c[0], c[2])
        if idx == 4: return (c[1], c[2], c[0])
        if idx == 5: return (c[1], -c[2], -c[0])
        if idx == 6: return (c[2], c[1], -c[0])
        if idx == 7: return (-c[2], -c[1], -c[0])
        if idx == 8: return (-c[2], c[0], -c[1])
        if idx == 9: return (c[2], -c[0], -c[1])
        if idx == 10: return (c[0], c[2], -c[1])
        if idx == 11: return (-c[0], -c[2], -c[1])
        if idx == 12: return (-c[0], c[1], -c[2])
        if idx == 13: return (-c[0], -c[1], c[2])
        if idx == 14: return (-c[1], c[0], c[2])
        if idx == 15: return (-c[1], -c[0], -c[2])
        if idx == 16: return (-c[1], c[2], -c[0])
        if idx == 17: return (-c[1], -c[2], c[0])
        if idx == 18: return (-c[2], c[1], c[0])
        if idx == 19: return (c[2], -c[1], c[0])
        if idx == 20: return (c[2], c[0], c[1])
        if idx == 21: return (-c[2], -c[0], c[1])
        if idx == 22: return (-c[0], c[2], c[1])
        if idx == 23: return (c[0], -c[2], c[1])

    def difference(a, b):
        return tuple([a[0]-b[0], a[1]-b[1], a[2]-b[2]])

    def addition(a, b):
        return tuple([a[0]+b[0], a[1]+b[1], a[2]+b[2]])

    def move_map(elem, diff, orientation):
        return set([addition(transform(e, orientation), diff) for e in elem])

    def match_map(original_elem, new_elem):
        for e1 in original_elem:
            for n1 in new_elem:
                for i in range(24):
                    diff = difference(e1, transform(n1, i))
                    new_map = move_map(new_elem, diff, i)
                    if len(new_map&original_elem) >= 12:
                        return new_map, diff

    checked = set()
    to_check = set()
    to_check.add(0)
    scanners = []
    new_inp = [set(i) for i in inp]
    while len(to_check) > 0:
        idx = to_check.pop()
        checked.add(idx)
        for i in range(len(new_inp)):
            if i in checked: continue
            elem = match_map(new_inp[idx], new_inp[i])
            if elem is not None:
                scanners.append(elem[1])
                to_check.add(i)
                new_inp[i] = elem[0]

    return new_inp, scanners

def part1(inp):
    inp, _ = get_correct_maps(inp)
    beacon_map = set()
    for i in inp:
        beacon_map |= i
    return len(beacon_map)


def part2(inp):
    def abs_diff(a, b):
        return tuple(sorted([abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2])]))

    _, scanners = get_correct_maps(inp)
    return max(sum(abs_diff(a,b)) for a,b in combinations(scanners, 2))

def prep_data(inp):
    data = []
    for l in inp:
        if l.strip():
            if "scanner" in l:
                    if "scanner 0" not in l:
                        data.append(res)
                        res = set()
                    else:
                        res = set()
            else:
                res.add(tuple(map(int, l.strip().split(","))))
    data.append(res)
    return data

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 79
print(part1(data))
assert part2(data_test) == 3621
print(part2(data))

