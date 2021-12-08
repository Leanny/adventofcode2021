from collections import Counter
def part1(inp):
    res = 0
    for i, o in inp:
        for val in o:
            if len(val) in [2, 3, 4, 7]:
                res += 1

    return res

def part2(inp):
    def translate_line(inpv, outv):
        current = list(Counter("".join(inpv)).items())
        translate_wire = {}
        translate = {}
        for i in inpv:
            if len(i) == 2:
                translate[1] = i
            elif len(i) == 3:
                translate[7] = i
            elif len(i) == 4:
                translate[4] = i
            elif len(i) == 7:
                translate[8] = i

        for k, v in current:
            if v == 6:
                translate_wire[1] = k
            if v == 9:
                translate_wire[5] = k
            if v == 4:
                translate_wire[4] = k

        translate_wire[2] = "".join(set(translate[1])-set([translate_wire[5]]))

        for i in inpv:
            if len(i) == 6:
                if not translate_wire[4] in i:
                    translate[9] = i
                elif translate_wire[2] in i:
                    translate[0] = i
                else:
                    translate[6] = i
            if len(i) == 5:
                if translate_wire[4] in i:
                    translate[2] = i
                elif translate_wire[1] in i:
                    translate[5] = i
                else:
                    translate[3] = i

        rev = {"".join(sorted(a)):b for b,a in translate.items()}
        num = 0
        for o in outv:
            num *= 10
            num += rev["".join(sorted(o))]
        return num
    return sum([translate_line(i, o) for i,o in inp])

def prep_data(inp):
    res = [(i.split("|")[0].strip().split(" "), i.strip().split("|")[1].strip().split(" ")) for i in inp]
    return res

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 26
print(part1(data))
assert part2(data_test) == 61229
print(part2(data))