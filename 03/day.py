from collections import Counter

def part1(input_data):
    counts = Counter()
    for c in input_data:
        counts.update([i for i,v in enumerate(c.strip()[::-1]) if v == "0"])
        
    slen = len(c.strip())
    gamma = 0
    threshold = len(input_data) // 2
    for k, v in counts.items():
        if v < threshold:
            gamma |= (1 << (k))
    epsilon = (2**slen)-1 - gamma
    return gamma * epsilon
    
def part2(input_data):
    all_inp = [list(map(int, i.strip())) for i in input_data]
    def get_val(inp, idx, val):
        #[1, 0] is a hack that ensures that 1 is in front when the counters are equal
        c = Counter([1, 0] + [i[idx] for i in inp])
        filter_val = c.most_common()[val][0]
        new_idx = [v for v in inp if v[idx] == filter_val]
        if len(new_idx) == 1:
            return int("".join(map(str, new_idx[0])), 2)
        return get_val(new_idx, idx+1, val)
        
    oxygen = get_val(all_inp, 0, 0)
    co2 = get_val(all_inp, 0, 1)
    return oxygen * co2
    
def prep_data(inp):
    return inp
    
with open("input_test.txt") as f:
    data = prep_data(f.readlines())
    
assert part1(data) == 198
assert part2(data) == 230

with open("input.txt") as f:
    data = prep_data(f.readlines())
    
print(part1(data))
print(part2(data))