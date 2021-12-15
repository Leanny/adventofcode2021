def generilize(inp, num):
    pairs, nums = inp

    for i in range(num):
        nums = {c: sum(nums[k] for k in pairs if c in pairs[k]) for c in nums}

    # since we have pairs with 2 outcomes each, each count will appear twice in the list
    all_counts = sorted([(sum(v * k.count(c[0]) for k, v in nums.items())+1)//2 for c in nums])

    return all_counts[-1] - all_counts[0]

def part1(inp):
    return generilize(inp, 10)

def part2(inp):
    return generilize(inp, 40)

def prep_data(inp):
    temp = [inp[0][i:i+2] for i in range(len(inp[0].strip())-1)]
    pairs = {k : (k[0] + v, v + k[1]) for k, v in [p.strip().split(' -> ') for p in inp[2:]]}
    nums = { k: temp.count(k) for k in pairs}
    return pairs, nums

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 1588
print(part1(data))
assert part2(data_test) == 2188189693529
print(part2(data))