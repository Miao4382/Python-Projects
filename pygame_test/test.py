import unittest
from solution import run_length_encode, run_length_decode

class TestStringMethods(unittest.TestCase):
	def test_encode(self):
		self.assertEqual(run_length_encode("A"), "A")
		self.assertEqual(run_length_encode("AA"), "A2")
		self.assertEqual(run_length_encode("AAA"), "A3")

	def test_decode(self):
		self.assertEqual(run_length_decode("A3"), "AAA")
		self.assertEqual(run_length_decode("A2"), "AA")
		self.assertEqual(run_length_decode("A"), "A")

	def test_README(self):
		self.assertEqual(run_length_encode("WWWABC"), "W3ABC")
		self.assertEqual(run_length_decode("W3ABC"), "WWWABC")
		self.assertEqual(run_length_encode("WWWWBBWWWWW"), "W4B2W5")
		self.assertEqual(run_length_decode("W4B2W5"), "WWWWBBWWWWW")

	def test_HARD(self):
		self.assertEqual(run_length_encode("WWWBBABBABABISLDSMMGHFGJFDMMMSMSSS"), "W3B2AB2ABABISLDSM2GHFGJFDM3SMS3")
		self.assertEqual(run_length_decode("Supercalifragilisticexpialidocious"), "Supercalifragilisticexpialidocious")

# Driver function
if __name__ == "__main__":
	unittest.main()

