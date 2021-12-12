from collections import Counter
def number_of_paths(inp, num):
    nodes, edges = inp
    results = []
    queue = [[1, "start"]]
    while len(queue) > 0:
        elem = queue.pop()
        mc = elem[0]
        for n in edges[elem[-1]]:
            if n == "start": continue
            if n == "end":
                results.append(elem + [n])
            elif nodes[n] or n not in elem or mc < num:
                res = elem + [n]
                # quick counter that abuses the fact that res[0] <= 2 for this task only
                if not nodes[n] and n in elem:
                    res[0] += 1
                queue.append(res)

    return len(results)

def part1(inp):
    return number_of_paths(inp, 1)

def part2(inp):
    return number_of_paths(inp, 2)

def prep_data(inp):
    edges = {}
    nodes = {}
    for line in inp:
        n1, n2 = line.strip().split("-")
        e1 = edges.get(n1, [])
        e1.append(n2)
        edges[n1] = e1
        e2 = edges.get(n2, [])
        e2.append(n1)
        edges[n2] = e2
        nodes[n1] =  n1 == n1.upper()
        nodes[n2] =  n2 == n2.upper()

    return nodes, edges

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 10
print(part1(data))
assert part2(data_test) == 36
print(part2(data))