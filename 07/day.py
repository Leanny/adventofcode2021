def part1(inp):
    def get_cost(inp, s):
        fuel = 0
        for i in inp:
            if i < s:
                fuel += s-i
            else:
                fuel += i-s
        return fuel 
    
    return min([get_cost(inp, i) for i in range(min(inp), max(inp)+1)])
    
def part2(inp):
    def get_cost(inp, s):
        fuel = 0
        for i in inp:
            if i < s:
                fuel += (s-i)*(s-i+1)//2
            else:
                fuel += (i-s)*(i-s+1)//2
        return fuel 
    
    return min([get_cost(inp, i) for i in range(min(inp), max(inp)+1)])

def prep_data(inp):
    res = list(map(int, inp[0].strip().split(",")))
    return res

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 37
print(part1(data))
assert part2(data_test) == 168
print(part2(data))