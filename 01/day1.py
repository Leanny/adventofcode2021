def generalize(input_data, sum_size):
    return len([i for i in range(sum_size, len(input_data)) if sum(input_data[i-sum_size:i]) < sum(input_data[i-sum_size+1:i+1])])

def part1(input_data):
    return generalize(input_data, 1)
    
def part2(input_data):
    return generalize(input_data, 3)
    
with open("input_test.txt") as f:
    data = list(map(int, f.readlines()))
    
assert part1(data) == 7
assert part2(data) == 5
 
with open("input.txt") as f:
    data = list(map(int, f.readlines()))
    
print(part1(data))
print(part2(data))