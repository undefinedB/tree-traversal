import unittest
from tree import Tree, Node

class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(1)
        self.tree.add(4)
        self.tree.add(6)
        self.tree.add(8)

    def test_find_existing(self):
        node = self.tree.find(4)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 4)

    def test_find_non_existing(self):
        node = self.tree.find(10)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()