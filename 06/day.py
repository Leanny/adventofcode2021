def generilize(days, inp):
    fish_cache = {}
    
    def generated_fish(d):
        # if we know how many fishes are generated, just return val
        if d in fish_cache: 
            return fish_cache[d]
        # end condition
        if d < 0:
            fish_cache[d] = 1
            return 1
            
        # normal fish cycle
        fish_cache[d - 7] = generated_fish(d - 7)
        # new fish cycle
        fish_cache[d - 9] = generated_fish(d - 9)
        return fish_cache[d - 7] + fish_cache[d - 9]
        
    return sum(generated_fish(days-f-1) for f in inp)
    
def part1(inp):
    return generilize(80, inp)
    
def part2(inp):
    return generilize(256, inp)

def prep_data(inp):
    res = list(map(int, inp[0].strip().split(",")))
    return res

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 5934
print(part1(data))
assert part2(data_test) == 26984457539
print(part2(data))