class RedBlackTree:
    class Node:
        def __init__(self, value, color='R'):
            self.value = value
            self.color = color  # 'R' = Red, 'B' = Black
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.TNULL = self.Node(value=None, color='B')
        self.root = self.TNULL

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, value):
        new_node = self.Node(value)
        new_node.left = self.TNULL
        new_node.right = self.TNULL

        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if new_node.value < x.value:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.value < y.value:
            y.left = new_node
        else:
            y.right = new_node

        new_node.color = 'R'
        self.fix_insert(new_node)

    def fix_insert(self, k):
        while k != self.root and k.parent.color == 'R':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.rotate_right(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.rotate_left(k.parent.parent)
        self.root.color = 'B'

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node == self.TNULL or value == node.value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def get_black_height(self):
        return self._get_black_height(self.root)

    def _get_black_height(self, node):
        if node == self.TNULL:
            return 1
        left_height = self._get_black_height(node.left)
        right_height = self._get_black_height(node.right)
        if left_height != right_height:
            raise ValueError("Tree is unbalanced")
        return left_height + (1 if node.color == 'B' else 0)

    def print_tree(self):
        from collections import deque

        def get_tree_depth(node):
            if node == self.TNULL:
                return 0
            return 1 + max(get_tree_depth(node.left), get_tree_depth(node.right))

        def node_repr(node):
            if node == self.TNULL:
                return "NIL"
            color = 'B' if node.color == 'B' else 'R'
            return f"{node.value}({color})"

        def print_level(level_nodes, level, max_depth):
            spacing = 2 ** (max_depth - level + 1)
            line = ' ' * (spacing // 2)
            between = ' ' * spacing
            line += between.join(level_nodes)
            print(line)

        max_depth = get_tree_depth(self.root)
        nodes = deque([(self.root, 1)])
        current_level = 1
        level_nodes = []

        while nodes:
            node, depth = nodes.popleft()
            if depth != current_level:
                print_level(level_nodes, current_level, max_depth)
                level_nodes = []
                current_level = depth
            level_nodes.append(node_repr(node))
            if depth <= max_depth:
                if node == self.TNULL:
                    nodes.append((self.TNULL, depth + 1))
                    nodes.append((self.TNULL, depth + 1))
                else:
                    nodes.append((node.left, depth + 1))
                    nodes.append((node.right, depth + 1))

        if level_nodes:
            print_level(level_nodes, current_level, max_depth)
rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)

print("Red-Black Tree:")
rb_tree.print_tree()
print("Black Height:", rb_tree.get_black_height())
