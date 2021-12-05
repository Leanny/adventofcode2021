from collections import Counter

def generalize(inp, diagonal=False):
    all_points = []
    
    for x1,y1,x2,y2 in inp:
        if x1 == x2:
            for i in range(y1, y2+1):
                all_points.append((x1, i))
        elif y1 == y2:
            for i in range(x1, x2+1):
                all_points.append((i, y1))
        elif diagonal:
            step = 1 if y1 < y2 else -1
            for i, x in enumerate(range(x1, x2+1)):
               all_points.append((x, y1+i*step))

    return len([1 for k,v in Counter(all_points).items() if v > 1]) 

def part1(inp):
    return generalize(inp, False)
    
def part2(inp):
    return generalize(inp, True) 

def prep_data(inp):
    res = []
    for i in inp:
        a,b = i.split("->")
        x1,y1 = map(int, a.strip().split(","))
        x2,y2 = map(int, b.strip().split(","))
        if x1 == x2 and y2 < y1: x1,y1,x2,y2 = x2,y2,x1,y1
        if y1 == y2 and x2 < x1: x1,y1,x2,y2 = x2,y2,x1,y1
        if x1 > x2 and y2 != y1: x1,y1,x2,y2 = x2,y2,x1,y1
        res.append((x1,y1,x2,y2))
    return res

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 5
assert part2(data_test) == 12

print(part1(data))
print(part2(data))