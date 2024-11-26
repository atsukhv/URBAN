import unittest

from module_12.module_12_1 import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("John")
        sirql = 0
        while sirql < 10:
            runner.walk()
            sirql += 1
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("John")
        sirql = 0
        while sirql < 10:
            runner.run()
            sirql += 1
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("John")
        runner2 = Runner("Otto")

        r1s = 0
        r2s = 0
        while r1s < 10 and r2s < 10:
            runner1.run()
            runner2.walk()
            r1s += 1
            r2s += 1
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()