class Students:
    def __init__(self, name="student", age="student", class_name="student"):

        self.name = name
        self.age = age
        self.class_name = class_name

    def get_avg_score(self, score_1, score_2, score_3):

        return (score_1 + score_2 + score_3) / 3


student_1 = Students("Jayden", 24, "DevOps")
print(student_1.name)

print(student_1.get_avg_score(20, 30, 20))
