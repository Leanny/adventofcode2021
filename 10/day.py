def part1(inp):
    def rate(line):
        queue = []
        for c in line:
            if c in opening:
                queue.append(c)
            elif c in closing:
                q = queue.pop(-1)
                if expected[q] != c:
                    return points[c]
        return 0

    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    opening = ["(", "[", "{", "<"]
    closing = list(points.keys())
    expected = {"(": ")", "{": "}", "[": "]", "<": ">"}
    s = 0
    for line in inp:
        s += rate(line)
    return s

def part2(inp):
    def fixLine(line):
        queue = []
        res = []
        for c in line:
            if c in opening:
                queue.append(c)
            elif c in closing:
                q = queue.pop(-1)
                if expected[q] != c:
                    return 0
            
        while len(queue) > 0:
            q = queue.pop(-1)
            res.append(expected[q])
        
        total = 0
        for r in res:
            total *= 5
            total += points[r]

        return total

    points = {")": 1, "]": 2, "}": 3, ">": 4}
    opening = ["(", "[", "{", "<"]
    closing = list(points.keys())
    expected = {"(": ")", "{": "}", "[": "]", "<": ">"}
    s = []
    for line in inp:
        r = fixLine(line)
        if r > 0:
            s.append(r)
    s = sorted(s)
    return s[len(s)//2]

def prep_data(inp):
    res = [i.strip() for i in inp]
    return res

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 26397
print(part1(data))
assert part2(data_test) == 288957
print(part2(data))