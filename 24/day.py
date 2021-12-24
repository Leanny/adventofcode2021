# use ALU for verification later
class ALU:
    def __init__(self):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def get_var(self, name):
        try:
            return int(name)
        except:
            if name == "x": return self.x
            if name == "y": return self.y
            if name == "z": return self.z
            if name == "w": return self.w

    def set_var(self, name, val):
        if name == "x": self.x = val
        if name == "y": self.y = val
        if name == "z": self.z = val
        if name == "w": self.w = val

    def inp(self, a, val):
        self.set_var(a, val)

    def add(self, a, b):
        self.set_var(a, self.get_var(a) + self.get_var(b))

    def mul(self, a, b):
        self.set_var(a, self.get_var(a) * self.get_var(b))

    def div(self, a, b):
        self.set_var(a, self.get_var(a) // self.get_var(b))

    def mod(self, a, b):
        self.set_var(a, self.get_var(a) % self.get_var(b))

    def eql(self, a, b):
        self.set_var(a, int(self.get_var(a) == self.get_var(b)))

def part(inp):
    def to_int(num):
        res = 0
        for n in num:
            res *= 10
            res += n
        return res

    def test_input(num):
        input_values = str(to_int(num))
        alu = ALU()
        i = 0
        for l in inp:
            if l[0] == "inp":
                alu.inp(l[1], int(input_values[i]))
                i += 1
            elif l[0] == "add":
                alu.add(l[1], l[2])
            elif l[0] == "mul":
                alu.mul(l[1], l[2])
            elif l[0] == "div":
                alu.div(l[1], l[2])
            elif l[0] == "rem":
                alu.mul(l[1], l[2])
            elif l[0] == "mod":
                alu.mod(l[1], l[2])
            elif l[0] == "eql":
                alu.eql(l[1], l[2])
        assert alu.z == 0

    # thanks to https://gitlab.com/asciiphil/advent-of-code/-/blob/master/2021/24.md
    vals = [list(map(int, (inp[i*18+4][-1], inp[i*18+5][-1], inp[i*18+15][-1]))) for i in range(14)]
    queue = []
    maxvals = [0] * 14
    minvals = [1] * 14
    for idx, (div, xadd, yadd) in enumerate(vals):
        if div == 1:
            queue.append((idx, yadd))
        else:
            idx2, y = queue.pop()
            delta = y + xadd
            if delta < 0:
                idx, idx2, delta = idx2, idx, -delta
            assert delta != 9

            maxvals[idx] = 9
            maxvals[idx2] = 9 - delta
            minvals[idx] = 1 + delta
            minvals[idx2] = 1


    test_input(maxvals)
    test_input(minvals)

    return str(to_int(maxvals)), str(to_int(minvals))

def prep_data(inp):
    data = [i.strip().split(" ") for i in inp]
    return data

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

res = part(data)
print(res[0])
print(res[1])