import math
import unittest
def wallis(n):
    p = 2

    for i in range(1,n+1):
        left = (2.0 * i)/(2. * i - 1.)
        right = (2.0 * i)/(2. * i + 1.)
        p = p * left * right
    # print(p)
    return p

def monte_carlo(n):
    import random
    cp=0
    sp=0
    for i in range(n):
        rx= random.uniform(-1, 1)
        ry= random.uniform(-1, 1)
        od= rx**2 + ry**2
        if od<= 1:
             cp+= 1
        sp+= 1
        p = 4* cp/ sp

    return p

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
