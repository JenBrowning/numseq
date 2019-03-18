import unittest
import prime
import geo
import fib


class Test(unittest.TestCase):

    def test_main(self):

        print ("Fibonacci")
        for i in range(10):
            print ("{}: {}".format(i, fib(i)))

        print("Geometric numbers (square, triangle, cube)")
        for i in range(10):
            print ("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))

        print ("Primes")
        prime_list = primes(1000)
        for p in prime_list[-10:]:
            print (p)
        print ("Is 999981 prime? {}".format(is_prime(999981)))
        print ("Is 999983 prime? {}".format(is_prime(999983)))


if __name__ == "__main__":
    unittest.main()
