class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self):
        return "Очень интересный вопрос, не знаю"


class Student(Human):
    def ask_question(self, someone, question):
        print(f'{someone.name}, {question}')
        someone.answer_question(question)
        print()


class Mentor(Human):
    def answer_question(self):
        return "Очень интересный вопрос, не знаю"