# Create a file called test_cities.py that tests the function you just wrote.
# Write a method called test_city_country() to verify that calling your function with values 
# such as 'santiago' and 'chile' results in the correct string.
# Run test_cities.py and make sure text_city_country() passes.

import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
	"""Tests for city_function.py"""

	def test_city_country(self):
		"""Does City, Country work?"""
		formatted_city_country = city_country('salt lake city', 'usa')
		self.assertEqual(formatted_city_country, 'Salt Lake City, Usa')

	def test_city_country_population(self):
		"""Does City, Country Population work?"""
		formatted_city_country_pop = city_country('salt lake city', 'usa', '200,544')
		self.assertEqual(formatted_city_country_pop, 'Salt Lake City, Usa 200,544')

if __name__ == '__main__':
	unittest.main()