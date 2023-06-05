class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self._insert_node(self.root, key)

    def _insert_node(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert_node(node.left, key)
        else:
            node.right = self._insert_node(node.right, key)

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        balance_factor = self._get_balance_factor(node)

        if balance_factor > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        elif balance_factor < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def export_to_graphviz(self, filename):
        with open(filename, "w") as file:
            file.write("digraph AVLTree {\n")
            file.write(
                "  node [shape=circle, style=filled, fillcolor=lightblue]\n")

            self._export_node(self.root, file)

            file.write("}\n")

    def _export_node(self, node, file):
        if node is None:
            return

        file.write(f'  {node.key} [label="{node.key} ({node.height})"]\n')

        if node.left is not None:
            file.write(f"  {node.key} -> {node.left.key}\n")
            self._export_node(node.left, file)

        if node.right is not None:
            file.write(f"  {node.key} -> {node.right.key}\n")
            self._export_node(node.right, file)


# Criação da árvore AVL
tree = AVLTree()

# Inserção de elementos na árvore
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

# Exportação da árvore para um arquivo Graphviz
tree.export_to_graphviz("avl_tree.dot")
