from django.test import TestCase
from app.calc import add, sub


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two nubmers are added together"""
        self.assertEqual(add(3, 8), 11)


    def test_sub_nubmer(self):
        """Subtract that two numbers are added together"""
        self.assertEqual(sub(6, 11), 5)
