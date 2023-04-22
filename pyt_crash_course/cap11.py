import unittest
from name_function import get_formatted_name

# utlizamos el modulo "unittest" para ordenar nuestros test unitarios
# utilizamos una funcion que esta en otro modulo 

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")

unittest.main()

