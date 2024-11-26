import unittest

from module_12.module_12_2 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    all_results = []

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = {place: str(runner) for place, runner in sorted(result.items())}
            print(formatted_result)

    def run_tournament(self, *participants):
        tournament = Tournament(90, *participants)
        results = tournament.start()
        self.all_results.append(results)
        return results

    def assert_last_runner(self, results, expected_name):
        self.assertTrue(max(results.keys()) in results and results[max(results.keys())] == expected_name)

    def test_race_usain_nik(self):
        results = self.run_tournament(self.runner1, self.runner3)
        self.assert_last_runner(results, "Ник")

    def test_race_andrey_nik(self):
        results = self.run_tournament(self.runner2, self.runner3)
        self.assert_last_runner(results, "Ник")

    def test_race_usain_andrey_nik(self):
        results = self.run_tournament(self.runner1, self.runner2, self.runner3)
        self.assert_last_runner(results, "Ник")

if __name__ == "__main__":
    unittest.main()