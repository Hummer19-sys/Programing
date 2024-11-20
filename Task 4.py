class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [grade]
            else:
                lecturer.lec_grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_value(self):
        total_sum = 0
        total_count = 0
        for value in self.grades.values():
            for number in value:
                total_sum += number
        for value in self.grades.values():
            total_count += len(value)
        return total_sum / total_count

    def __str__(self):
        result = (
            f"CТУДЕНТ\n"
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Курсы в процесе изучения: {','.join(map(str, self.courses_in_progress))}\n"
            f"Завершенные курсы: Введение в программирование\n"
            f"Средняя оценка за домашние задания: {self.middle_value()}\n"
        )
        return result

    def __lt__(self, other):
        for course, grades in self.grades.items():
            return self.middle_value() < other.middle_value()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lec_grades = {}

    def middle_value(self):
        total_sum = 0
        total_count = 0
        for value in self.lec_grades.values():
            for number in value:
                total_sum += number
        for value in self.lec_grades.values():
            total_count += len(value)
        return total_sum / total_count

    def  __str__(self):
        result = (
            f"ЛЕКТОР\n"
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.middle_value()}\n"
        )
        return result

    def __lt__(self, other):
        for course, grades in self.lec_grades.items():
            return self.middle_value() < other.middle_value()


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


best_student = Student('Roy', 'Jones', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

just_student = Student('Mike', 'Tyson', 'man')
just_student.courses_in_progress += ['Python']
just_student.courses_in_progress += ['Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

just_reviewer = Reviewer('Once', 'Toldme')
just_reviewer.courses_attached += ['Python']
just_reviewer.courses_attached += ['Git']

cool_lecturer = Lecturer('The', 'World')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

just_lecturer = Lecturer('Isgonna', 'Rollme')
just_lecturer.courses_attached += ['Python']
just_lecturer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Git', 9)

cool_reviewer.rate_hw(just_student, 'Python', 8)
cool_reviewer.rate_hw(just_student, 'Git', 10)

best_student.rate_lec(cool_lecturer, 'Python', 10)
best_student.rate_lec(cool_lecturer, 'Git', 9)

best_student.rate_lec(just_lecturer, 'Python', 9)
best_student.rate_lec(just_lecturer, 'Git', 7)

students = [best_student, just_student]
lecturers = [cool_lecturer, just_lecturer]

def average_grade_for_course(student, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    return 0

def average_lecture_grade_for_course(lecturer, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.lec_grades:
            total_grades.extend(lecturer.lec_grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    return 0

print(f"Средняя оценка студентов по Python: {average_grade_for_course(student=students,course='Python')}")
print(f"Средняя оценка студентов по Git: {average_grade_for_course(student=students,course='Git')}")

print(f"Средняя оценка лекторов по Python: {average_lecture_grade_for_course(lecturer=lecturers, course='Python')}")
print(f"Средняя оценка лекторов по Git: {average_lecture_grade_for_course(lecturer=lecturers ,course='Git')}")

is_lt = (best_student < cool_lecturer)
print(f"Средняя оценка студента за домашние задания ниже, чем средняя оценка лектора: {is_lt}\n")

print(best_student)
print(cool_lecturer)
print(cool_reviewer)