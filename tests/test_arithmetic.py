from unittest import TestCase

from arithmetic import gcd, lcm


class ArithmeticTestCase(TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 36), 12)
        self.assertEqual(gcd(0, 36), 36)
        self.assertEqual(gcd(36, 0), 36)
        self.assertEqual(gcd(0, 0), 0)
