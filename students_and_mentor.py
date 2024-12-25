class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer) and
            course in self.courses_in_progress and
            course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        grades_list = [grade for grades in self.grades.values() for grade in grades]
        return sum(grades_list) / len(grades_list) if grades_list else 0

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        avg_grade = self.get_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        grades_list = [grade for grades in self.grades.values() for grade in grades]
        return sum(grades_list) / len(grades_list) if grades_list else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student) and
            course in self.courses_attached and
            course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

# Создаем студентов
student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']

student_2 = Student('Anna', 'Smith', 'female')
student_2.courses_in_progress += ['Python']

# Создаем лекторов
lecturer_1 = Lecturer('John', 'Doe')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Jane', 'Roe')
lecturer_2.courses_attached += ['Python']

# Создаем экспертов
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Alice', 'Wonder')
reviewer_2.courses_attached += ['Python']

# Эксперты оценивают студентов
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 7)

# Студенты оценивают лекторов
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_2, 'Python', 8)
student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 7)

# Вывод информации
print(reviewer_1)
print()
print(reviewer_2)
print()
print(student_1)
print()
print(student_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()

# Подсчет средней оценки
print(f"Средняя оценка за домашние задания по курсу Python: {average_student_grade([student_1, student_2], 'Python'):.1f}")
print(f"Средняя оценка за лекции по курсу Python: {average_lecturer_grade([lecturer_1, lecturer_2], 'Python'):.1f}")
