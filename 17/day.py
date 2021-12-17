import math

def part1(inp):
    x, y = inp
    return -y[0]*(-y[0]-1)//2

def part2(inp):
    def get_pos(velx, vely, t):
        res_x = velx * t - t * (t - 1) // 2 if t < velx else velx * (velx + 1) // 2
        res_y = vely * t - t * (t - 1) // 2
        return res_x, res_y

    def is_intersecting(px, py):
        t_min = math.floor(py + math.sqrt(py * py - 2 * y[1]))
        t_max = math.floor(py + math.sqrt(py * py - 2 * y[0]))
        for t in range(t_min, t_max+2):
            rx, ry = get_pos(px, py, t)
            if x[0] <= rx <= x[1] and y[0] <= ry <= y[1]:
                return True

    x, y = inp
    return len([1 for px in range(math.floor(math.sqrt(x[0])-1), x[1]+1) for py in range(y[0], -y[0]) if is_intersecting(px, py)]

def prep_data(inp):
    data = inp[0].strip()[len("target area: "):].split(",")
    x = list(map(int, data[0][2:].split("..")))
    y = list(map(int, data[1][3:].split("..")))
    return x, y

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 45
print(part1(data))
assert part2(data_test) == 112
print(part2(data))
