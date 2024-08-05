import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        # Тестирование существующего индекса
        self.assertEqual(arrs.get([1, 2, 3], 1), 2)

        # Тестирование несуществующего индекса
        self.assertEqual(arrs.get([1, 2, 3], 3), None)
        self.assertEqual(arrs.get([1, 2, 3], -1), None)

        # Тестирование значения по умолчанию
        self.assertEqual(arrs.get([1, 2, 3], 3, "default"), "default")
        self.assertEqual(arrs.get([], 0, "default"), "default")

    def test_slice(self):
        # Тестирование среза с заданными start и end
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])

        # Тестирование среза с None в качестве start
        self.assertEqual(arrs.my_slice([1, 2, 3], None, 2), [1, 2])

        # Тестирование среза с None в качестве end
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, None), [2, 3])

        # Тестирование среза с пустым списком
        self.assertEqual(arrs.my_slice([], None, None), [])

        # Тестирование среза, когда start больше длины
        self.assertEqual(arrs.my_slice([1, 2, 3], 5, 10), [])

        # Тестирование среза, когда end меньше длины
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, 1), [1])

