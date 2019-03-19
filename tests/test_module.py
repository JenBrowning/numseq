#!/usr/bin/env python
# -*- coding: utf-8 -*-

# with help from Piero 

import os
import unittest
import sys
sys.path.insert(0, os.path.abspath('..'))
from numseq.fib import *
from numseq.geo import *
from numseq.prime import *


class TestNumSeq(unittest.TestCase):

    def test_fib(self):

        print("Fibonacci")
        for i in range(10):
            print("{}: {}".format(i, fib(i)))
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(10), 55)

    def test_geo(self):

        print("Geometric numbers (square, triangle, cube)")
        for i in range(10):
            print("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))
        self.assertEqual(square(4), 16)
        self.assertEqual(square(7), 49)
        self.assertEqual(triangle(4), 10)
        self.assertEqual(triangle(7), 28)
        self.assertEqual(cube(7), 343)
        self.assertEqual(cube(9), 729)


    def test_primes(self):
        print("Primes")
        prime_list = primes(1000)
        for p in prime_list[-10:]:
            print(p)
        self.assertFalse(is_prime(999981))
        self.assertTrue(is_prime(999983))
        self.assertSequenceEqual(
            primes(1000)[-10:], [937, 941, 947, 953, 967, 971, 977, 983, 991, 997])

# print("Is 999981 prime? {}".format(is_prime(999981)))
# print("Is 999983 prime? {}".format(is_prime(999983)))


if __name__ == "__main__":
    unittest.main()
