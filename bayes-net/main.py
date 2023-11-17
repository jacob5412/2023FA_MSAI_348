"""
Bayesian Network Unit Tests

This test suite contains unit tests for the functionalities of the Bayesian Network module. It verifies the correctness
of the 'ask' function from the 'joint_probs' module, specifically its behavior when querying probabilities in a predefined
Bayesian Network scenario involving burglary, alarm, calls, and earthquakes.

Classes:
- BayesTest: Inherits from unittest.TestCase and includes test methods for various scenarios in the Bayesian Network.

Usage:
1. Create a BayesTest object: test_suite = BayesTest()
2. Run individual tests: test_suite.test1(), test_suite.test2(), ..., test_suite.test5()
3. Execute the entire test suite by running this file: python filename.py

Each test checks the calculated probability against an expected value, ensuring the correctness of the Bayesian
Network's inference capabilities.

Example:
    test_suite = BayesTest()
    test_suite.test1()

This suite helps validate the accuracy of the Bayesian Network's reasoning in different scenarios for informed
decision-making and probabilistic analysis.
"""

import unittest

from bayesnet import BayesNet, BayesNode
from joint_probs import ask


class BayesTest(unittest.TestCase):
    def makeBurglaryNet(self):
        bn = BayesNet()
        bn.add(BayesNode("Burglar", None, {"": 0.001}))
        bn.add(BayesNode("Earthquake", None, {"": 0.002}))
        bn.add(
            BayesNode(
                "Alarm",
                ["Burglar", "Earthquake"],
                {
                    (False, False): 0.001,
                    (False, True): 0.29,
                    (True, False): 0.94,
                    (True, True): 0.95,
                },
            )
        )
        bn.add(BayesNode("JohnCalls", ["Alarm"], {True: 0.9, False: 0.05}))
        bn.add(BayesNode("MaryCalls", ["Alarm"], {True: 0.7, False: 0.01}))
        return bn

    def test1(self):
        bn = self.makeBurglaryNet()
        a = ask("Alarm", True, {"Burglar": True, "Earthquake": True}, bn)
        print("P(a|b,e)=", a)
        self.assertAlmostEqual(0.95, a)

    def test2(self):
        bn = self.makeBurglaryNet()
        a = ask("Burglar", True, {"JohnCalls": True, "MaryCalls": True}, bn)
        print("P(b|j,m)=", a)
        self.assertAlmostEqual(0.2841718, a)

    def test3(self):
        bn = self.makeBurglaryNet()
        a = ask("Alarm", True, {}, bn)
        print("P(a)=", a)
        self.assertAlmostEqual(0.002516442, a)

    def test4(self):
        bn = self.makeBurglaryNet()
        a = ask("Alarm", True, {"Burglar": False}, bn)
        print("P(a|-b)=", a)
        self.assertAlmostEqual(0.001578, a)

    def test5(self):
        bn = self.makeBurglaryNet()
        a = ask("Earthquake", False, {"Burglar": True}, bn)
        print("P(-e)=", a)
        self.assertAlmostEqual(0.998, a)


if __name__ == "__main__":
    unittest.main()
