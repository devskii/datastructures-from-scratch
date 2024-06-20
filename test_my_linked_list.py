import unittest
from my_linked_list import MyLinkedList


class TestLengthOne(unittest.TestCase):
    def setUp(self):
        self.my_linked_list = MyLinkedList(1)

    def test_to_string(self):
        self.assertEqual(self.my_linked_list.to_string(), "1")


class TestLargerExample(unittest.TestCase):
    def setUp(self):
        ll = MyLinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        self.my_linked_list = ll

    def test_to_string(self):
        self.assertEqual(self.my_linked_list.to_string(), "1 2 3 4")

    def test_remove_from_beginning(self):
        ll = self.my_linked_list.remove(1)
        self.assertEqual(ll.to_string(), "2 3 4")

    def test_remove_from_middle(self):
        ll = self.my_linked_list.remove(3)
        self.assertEqual(ll.to_string(), "1 2 4")

    def test_remove_from_end(self):
        ll = self.my_linked_list.remove(4)
        self.assertEqual(ll.to_string(), "1 2 3")

    def test_remove_null(self):
        ll = self.my_linked_list.remove(None)
        self.assertEqual(ll.to_string(), "1 2 3 4")


if __name__ == "__main__":
    unittest.main()
