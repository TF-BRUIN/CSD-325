import unittest
from city_functions import city_country

class LocationTestCase(unittest.TestCase):
	def test_city_country(self):
		print("Running test...")
		complete_name = city_country("Havana", "Cuba")
		self.assertEqual(complete_name, "Havana, Cuba")
		print("Test complete.")

if __name__ == '__main__':
	unittest.main()



