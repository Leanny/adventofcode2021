import json

class SnailfishTree:
    def __init__(self):
        self.parent: SnailfishTree = None
        self.left: SnailfishTree = None
        self.right: SnailfishTree = None
        self.value: int = None
        self.depth: int = 0

    def set_depth(self):
        if self.parent is not None:
            self.depth = self.parent.depth + int(self.value is None)
        if self.value is None:
            self.left.set_depth()
            self.right.set_depth()

    def append_left(self, node):
        self.left = node
        node.parent = self

    def append_right(self, node):
        self.right = node
        node.parent = self

    def explode_all(self):
        if self.value is None:
            if self.depth >= 4 and self.left.value is not None and self.right.value is not None:
                self.explode()
                return True
            return self.left.explode_all() or self.right.explode_all()

    def split_all(self):
        if self.value is None:
            return self.left.split_all() or self.right.split_all()
        else:
            if self.value >= 10:
                self.split()
                return True

    def reduce(self):
        return self.explode_all() or self.split_all()

    def reduce_all(self):
        while self.reduce():
            pass

    def explode(self):
        lv = self.left.value
        rv = self.right.value

        curr = self
        while curr.parent is not None and curr.parent.left == curr:
            curr = curr.parent
        if curr.parent is not None:
            curr = curr.parent.left
            while curr.value is None:
                curr = curr.right
            curr.value += lv

        curr = self
        while curr.parent is not None and curr.parent.right == curr:
            curr = curr.parent
        if curr.parent is not None:
            curr = curr.parent.right
            while curr.value is None:
                curr = curr.left
            curr.value += rv

        st = SnailfishTree()
        st.depth = self.depth
        st.value = 0
        st.parent = self.parent
        if self.parent.left == self:
            self.parent.left = st
        else:
            self.parent.right = st

    def split(self):
        lv = self.value // 2
        rv = self.value - lv
        st = SnailfishTree()
        st.depth = self.depth + 1
        st.value = None
        st.parent = self.parent
        if self.parent.left == self:
            self.parent.left = st
        else:
            self.parent.right = st
        leftNode = SnailfishTree()
        rightNode = SnailfishTree()
        leftNode.depth = st.depth
        rightNode.depth = st.depth
        leftNode.value = lv
        rightNode.value = rv
        st.append_left(leftNode)
        st.append_right(rightNode)


    @staticmethod
    def parse_expr(expr):
        def create_tree(expr):
            st = SnailfishTree()
            if type(expr) is list:
                st.append_left(create_tree(expr[0]))
                st.append_right(create_tree(expr[1]))
            else:
                st.value = expr
            return st
        tree = create_tree(expr)
        tree.set_depth()
        return tree

    def add_fish(self, other):
        st = SnailfishTree()
        st.append_left(SnailfishTree.parse_expr(self.list_repr()))
        st.append_right(SnailfishTree.parse_expr(other.list_repr()))
        st.set_depth()
        st.reduce_all()

        return st

    def list_repr(self):
        if self.value is None:
            return json.loads(f"[{self.left.list_repr()}, {self.right.list_repr()}]")
        return self.value

    def get_magnitude(self):
        if self.value is None:
            return 3 * self.left.get_magnitude() + 2 * self.right.get_magnitude()
        return self.value

    def __str__(self):
        return json.dumps(self.list_repr())

    def __repr__(self):
        return str(self)

def part1(inp):
    res = inp[0]
    for i in range(1, len(inp)):
        res = res.add_fish(inp[i])

    return res.get_magnitude()

def part2(inp):
    res = [inp[i].add_fish(inp[j]).get_magnitude() for i in range(len(inp)) for j in range(len(inp)) if i != j]
    return max(res)

def prep_data(inp):
    data = [SnailfishTree.parse_expr(json.loads(i.strip())) for i in inp]
    return data

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 4140
print(part1(data))
assert part2(data_test) == 3993
print(part2(data))
