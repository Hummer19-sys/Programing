class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer , Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [grade]
            else:
                lecturer.lec_grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_value(self, course):
        if course in self.grades:
            return sum(self.grades[course]) / len(self.grades[course])
        else:
            return 0

    def __str__(self):
        result = (
            f"CТУДЕНТ\n"
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Курсы в процесе изучения: {','.join(map(str, self.courses_in_progress))}\n"
            f"Завершенные курсы: Введение в программирование\n"
        )
        for course, grades in self.grades.items():
            average = self.middle_value(course)
            result += f"Средняя оценка за домашние задания: {average:.2f}\n"
        return result

    def __lt__(self, other):
        for course, grades in self.grades.items():
            return self.middle_value(course) < other.middle_value(course)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lec_grades = {}

    def middle_value(self, course):
        if course in self.lec_grades:
            return sum(self.lec_grades[course]) / len(self.lec_grades[course])
        else:
            return 0

    def  __str__(self):
        result = (
            f"ЛЕКТОР\n"
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
        )
        for course, grades in self.lec_grades.items():
            average = self.middle_value(course)
            result += f"Средняя оценка за лекции: {average:.2f}\n"
        return result

    def __lt__(self, other):
        for course, grades in self.lec_grades.items():
            return self.middle_value(course) < other.middle_value(course)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def  __str__(self):
        return (f"ПРОВЕРЯЮЩИЙ\n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']


cool_lecturer = Lecturer('Roy', 'Jones')
cool_lecturer.courses_attached += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)


best_student.rate_lec(cool_lecturer, 'Python', 10)
best_student.rate_lec(cool_lecturer, 'Python', 9)

is_lt = (best_student < cool_lecturer)
print(f"Средняя оценка студента за домашние задания ниже, чем средняя оценка лектора: {is_lt}\n")


print(best_student)
print(cool_lecturer)
print(cool_reviewer)