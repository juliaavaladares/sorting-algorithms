from node import *


class AVLTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, val):
        if (not node):
            return Node(val)
        else:
            if (val > node.key):
                node.right = self._insert(node.right, val)
            elif (val < node.key):
                node.left = self._insert(node.left, val)
            else:
                return node

            self._update_height(node)
            node = self._balance(node)
            return node

    def _update_height(self, node):
        node.height = max(self._get_height(node.left),
                          self._get_height(node.right)) + 1

    def _get_height(self, node):
        if node is None:
            return 0

        return node.height

    def _balance(self, node):
        balance_factor = self._get_balance_factor(node)

        if (balance_factor > 1 and self._get_balance_factor(node.left) >= 0):  # LL
            return self._right_rotate(node)
        elif (balance_factor > 1 and self._get_balance_factor(node.left) < 0):  # LR
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        elif (balance_factor < -1 and self._get_balance_factor(node.right) <= 0):  # RR
            return self._left_rotate(node)
        elif (balance_factor < -1 and self._get_balance_factor(node.right) > 0):  # RL
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        else:
            return node

    def _get_balance_factor(self, node):
        if node is None:
            return 0

        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        self._update_height(node)
        self._update_height(right_child)
        return right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        self._update_height(node)
        self._update_height(left_child)
        return left_child

    def print_avl_tree(self):
        if self.root is None:
            return

        self._print_avl_tree_helper(self.root)

    def _print_avl_tree_helper(self, node):
        if node is not None:
            self._print_avl_tree_helper(node.left)
            print(node.key, node.height)
            self._print_avl_tree_helper(node.right)

    def search(self, key):
        if self.root is None:
            return None
        else:
            return self._search(self.root, key)

    def _search(self, node, key):
        if node.key.strip(" ") == key:
            return node
        elif key < node.key and node.left is not None:
            return self._search(node.left, key)
        elif key > node.key and node.right is not None:
            return self._search(node.right, key)
        else:
            return None

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

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _next(self, node):
        if (not node):
            return None
        if (not node.right):
            return None
        cur_node = node.right
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node

    def _delete(self, node, target):
        if (not node):
            return None

        res_node = None
        if (target > node.val):
            node.right = self._delete(node.right, target)
            res_node = node
        elif (target < node.val):
            node.left = self._delete(node.left, target)
            res_node = node
        else:
            if not node.left:
                res_node = node.right
            elif not node.right:
                res_node = node.left
            else:
                next_node = self._next(node)
                next_node.right = self._delete(node.right, next_node.val)
                next_node.left = node.left
                res_node = next_node

        if (not res_node):
            return None
        self._update_height(res_node)
        self._balance(res_node)
        return res_node

    def delete(self, val):
        self.root = self._delete(self.root, val)
