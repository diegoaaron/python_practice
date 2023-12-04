def get_formatted_name(first, last, middle = ""):
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

# Clase a testear

class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("survey results")
        for response in self.responses:
            print("- " + response)


