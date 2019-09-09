import unittest
from api import get_players
from api import get_player_stats


class QueryTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    #Edge Case tests for get_players method
    def test_get_players(self):
        result = get_players("LeBron James")
        self.assertTrue(result[0]["end_year"] == 2018)

    def test_get_players_substring(self):
        result = get_players("LeBro")
        self.assertTrue(result[0]["end_year"] == 2018)

    def test_get_players_typeerror(self):
        with self.assertRaises(TypeError):
            get_players(1)

    def test_get_players_case(self):
        result = get_players("lebron james")
        self.assertTrue(result[0]["end_year"] == 2018)

    def test_get_players_multiple(self):
        result = get_players("Gasol")
        self.assertTrue(result[0]["player_name"] == "Marc Gasol" and result[1]["player_name"] == "Pau Gasol")

    def test_get_players_empty(self):
        result = get_players("absdgsdfkjsdhfslh")
        self.assertTrue(result == [])

    #Edge Case tests for get_player_stats method

    def test_player_stats(self):
        with self.assertRaises(TypeError):
            get_player_stats(-1)

    def test_player_stats(self):
        results = get_player_stats('Alvan Adams')
        self.assertTrue(results[0]["pts"] == 1202)


if __name__ == '__main__':
    unittest.main()