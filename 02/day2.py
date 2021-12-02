def part1(input_data):
    h, v = 0, 0
    for f,u,d in input_data:
        if f:
            h += d
        else :
            v += u*d
    return h*v
    
def part2(input_data):
    a, h, v = 0, 0, 0
    for f,u,d in input_data:
        if f:
            h += d
            v += a*d
        else :
            a += u*d
    return h*v
    
def prep_data(i):
    a,b = i.strip().split(" ")
    return a[0] == "f", 1 if a[0] == "d" else -1, int(b)
    
with open("input_test.txt") as f:
    data = [prep_data(i) for i in f.readlines()]
    
assert part1(data) == 150
assert part2(data) == 900

with open("input.txt") as f:
    data = [prep_data(i) for i in f.readlines()]
    
print(part1(data))
print(part2(data))