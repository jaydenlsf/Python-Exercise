def calc_grade(name, homework, assessment, exam):
    homework *= 4
    assessment *= 2

    ict_per = (homework + assessment + exam) / 3

    grade_dict = {
        "D": range(40, 50),
        "C": range(50, 60),
        "B": range(60, 70),
        "A": range(70, 100),
    }

    for grade, per in grade_dict.items():
        if ict_per < 40:
            ict_grade = "Failed"
            break
        elif ict_per > 100:
            ict_grade = "Invalid score entries."
            break
        elif int(ict_per) in per:
            ict_grade = grade

    return round(ict_per, 2), ict_grade


name = input("What's your name?: ")
homework = int(input("Homework score (/25): "))
assessment = int(input("Assessment score (/50): "))
exam = int(input("Final exam score (/100): "))

print(calc_grade(name, homework, assessment, exam))
