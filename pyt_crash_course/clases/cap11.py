import unittest
from name_function import get_formatted_name, AnonymousSurvey

# utlizamos el modulo "unittest" para ordenar nuestros test unitarios
# debemos utilizar la palabra 'test_' en cada metodo test creado para que
# sea llamado automaticamente al ejecutar el test 

# utilizamos una funcion que esta en otro modulo 

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


# testeando la clase AnonymousSurvey

class TestAnonymousSurve(unittest.TestCase):

    def test_store_single_response(self):
        question = "cual es tu primer idioma: "
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")

        self.assertIn("English", my_survey.responses)

    def test_store_three_response(self):
        question = "cual es tu primer idioma: "
        my_survey = AnonymousSurvey(question)
        responses = ["English", "Spanish", "Mandarin"]
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()