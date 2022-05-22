import unittest
import booting_game
import word_guessing


class TestCase(unittest.TestCase):
    def test_booting(self):
        choosed = booting_game.game_mode()
        self.assertEqual(choosed, [1, 1, 1])

    def test_finding_word(self):
        word = word_guessing.find_word([1, 1, 1])
        self.assertTrue(len(word) <= 5)
    

if __name__ == '__main__':
    unittest.main()
