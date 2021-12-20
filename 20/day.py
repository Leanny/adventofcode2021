from collections import defaultdict

def general(inp, num):
    def get_as_arr(arr):
        x_val = [x for x, y in arr]
        y_val = [y for x, y in arr]
        xmin = min(x_val)
        xmax = max(x_val)
        ymin = min(y_val)
        ymax = max(y_val)
        xlen = xmax-xmin+1
        ylen = ymax-ymin+1
        res = [[arr[(x+xmin, y+ymin)] for y in range(ylen)] for x in range(xlen)]
        return res

    def print_arr(arr):
        t = {".": 0, "#": 1, 0: ".", 1: "#"}
        res = get_as_arr(arr)

        for i in res:
            print("".join(map(t.get, i)))
        print("")

    def get_pixel(x, y, image, nchr):
        def get_px(im, x, y):
            if x < 0: return nchr
            if y < 0: return nchr
            if x >= len(im): return nchr
            if y >= len(im[0]): return nchr
            return image[x][y]

        num = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                num <<= 1
                num += get_px(image, i, j)

        return translation[num]

    def get_ones(arr):
        return len([pos for pos, val in arr.items() if val == 1])

    def apply_scaling(img, nchr):
        def get_neighbours(x, y):
            yield x-1, y-1
            yield x-1, y
            yield x-1, y+1
            yield x, y-1
            yield x, y
            yield x, y+1
            yield x+1, y-1
            yield x+1, y
            yield x+1, y+1

        output = defaultdict(lambda: nchr)
        as_arr = get_as_arr(img)
        #print_arr(img)
        relevant = set()
        for x in range(-1, len(as_arr)+1):
            for y in range(-1, len(as_arr[0])+1):
                output[(x, y)] = get_pixel(x, y, as_arr, nchr)

        return output

    translation, image = inp
    img = image
    null_chr = 0
    for _ in range(num):
        null_chr = 511 - null_chr if translation[0] == 1 else 0
        img = apply_scaling(img, translation[null_chr])

    return get_ones(img)

def part1(inp):
    return general(inp, 2)

def part2(inp):
    return general(inp, 50)

def prep_data(inp):
    t = {".": 0, "#": 1}
    translation = [t[i] for i in inp[0].strip()]
    image = defaultdict(int)
    for i, p1 in enumerate(inp[2:]):
        for j, p2 in enumerate(p1.strip()):
            image[(i, j)] = t[p2]
    return translation, image

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 35
print(part1(data))
assert part2(data_test) == 3351
print(part2(data))
