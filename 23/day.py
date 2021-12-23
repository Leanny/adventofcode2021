from queue import PriorityQueue, Queue

def solve(inp):
    def get_moves(state, cost):
        def occupied(start, end):
            for j in range(start, end):
                if len(state[j]):
                    return True
            for j in range(end + 1, start+ 1):
                if len(state[j]):
                    return True
            return False

        additional_costs = {"A": 1, "B": 10, "C": 100, "D": 1000}
        base_res = {"A": 0, "B": 1, "C": 2, "D": 3}
        out_pos = [2, 4, 6, 8]
        freeze = list(state)
        for i, f in enumerate(state):
            if len(f):
                if i < 11:
                    if occupied(out_pos[base_res[f]], i): continue
                    base_pos = base_res[f] + 7 + 4 * var_len
                    add_cost = var_len
                    while base_pos > 10:
                        if len(state[base_pos]) and state[base_pos] != f: break
                        if len(state[base_pos]) == 0 and (base_pos < 15 or len(state[base_pos-4]) == 0):
                            freeze[i], freeze[base_pos] = freeze[base_pos], freeze[i]
                            steps = add_cost + abs(out_pos[base_res[f]] - i)
                            yield freeze, additional_costs[f] * steps + cost
                            freeze[i], freeze[base_pos] = freeze[base_pos], freeze[i]
                            break
                        base_pos -= 4
                        add_cost -= 1
                elif i < 15 or len(state[i-4]) == 0:
                    steps_out = (i-11)//4+1
                    pos_out = out_pos[i - 4 * steps_out - 7]
                    for k in [0, 1, 3, 5, 7, 9, 10]:
                        if len(state[k]): continue
                        if occupied(pos_out, k): continue
                        freeze[i], freeze[k] = freeze[k], freeze[i]
                        steps = steps_out + abs(pos_out - k)
                        yield freeze, additional_costs[f] * steps + cost
                        freeze[i], freeze[k] = freeze[k], freeze[i]

    var_len = len(inp)
    field = [""] * 11
    for i in inp:
        field.extend(i)
    field = tuple(field)
    goal_state = [""] * 11 + ["A", "B", "C", "D"] * var_len
    possible_states = PriorityQueue()
    possible_states.put((0, field))
    visited = set()
    goals = None
    while not possible_states.empty():
        cost, state = possible_states.get()
        if goals is not None and cost > goals: continue
        if state in visited: continue
        visited.add(state)
        for s, c in get_moves(state, cost):
            if goals is not None and c > goals: continue
            if s == goal_state:
                if goals is None or goals > c:
                    goals = c
            else:
                q = tuple(s)
                if q not in visited:
                    possible_states.put((c, q))

    return goals

def part1(inp):
    return solve(inp)

def part2(inp):
    inp.insert(1, "DCBA")
    inp.insert(2, "DBAC")
    return solve(inp)

def prep_data(inp):
    data = [inp[2].strip().replace("#", ""), inp[3].strip().replace("#", "")]
    return data

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

from time import time
start = time()
assert part1(data_test) == 12521
print(part1(data))
assert part2(data_test) == 44169
print(part2(data))
print(time()-start)
