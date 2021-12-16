class BINReader:
    def __init__(self, inp):
        self.bin_inp = bin(int(inp, 16))[2:]
        v = int(inp[0], 16) >> 1
        if v < 2:
            self.bin_inp = "0" + self.bin_inp
        if v < 4:
            self.bin_inp = "0" + self.bin_inp
        self.total_ver = 0
        self.i = 0

    def read_bytes(self, num):
        res = self.bin_inp[self.i:self.i+num]
        self.i += num
        return res

    def read_num(self):
        res = ""
        while self.read_bytes(1) == "1":
            res += self.read_bytes(4)
        res += self.read_bytes(4)
        result = int(res, 2)
        return result

    def read_package(self):
        v = int(self.read_bytes(3), 2)
        t = int(self.read_bytes(3), 2)
        self.total_ver += v
        if t == 4:
            return self.read_num()
        else:
            lid = self.read_bytes(1)
            sub_vals = []
            if lid == "0":
                sub_length = int(self.read_bytes(15), 2)
                end = self.i + sub_length
                while self.i < end:
                    res = self.read_package()
                    sub_vals.append(res)
            else:
                sub_length = int(self.read_bytes(11), 2)
                for _ in range(sub_length):
                    res = self.read_package()
                    sub_vals.append(res)

            if t == 0:
                return sum(sub_vals)
            elif t == 1:
                res = 1
                for s in sub_vals:
                    res *= s
                return res
            elif t == 2:
                return min(sub_vals)
            elif t == 3:
                return max(sub_vals)
            elif t == 5:
                return int(sub_vals[0] > sub_vals[1])
            elif t == 6:
                return int(sub_vals[0] < sub_vals[1])
            elif t == 7:
                return int(sub_vals[0] == sub_vals[1])

def part1(inp):
    br = BINReader(inp)
    br.read_package()
    return br.total_ver

def part2(inp):
    br = BINReader(inp)
    return br.read_package()

def prep_data(inp):
    return inp[0].strip()

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 20
print(part1(data))
assert part2(data_test) == 1
print(part2(data))