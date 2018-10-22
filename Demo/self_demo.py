class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.name, self.score)


a = Student("11", 22)
a.print_score()
