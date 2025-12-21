class GroupLimitError(Exception):
    """Виняток, який виникає, якщо в групі більше 10 студентів."""
    pass


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.record_book})"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        # Якщо студент уже є у set, додавання нічого не змінить
        # тому ліміт перевіряємо так: якщо студента немає і місць вже 10 -> помилка
        if student not in self.group and len(self.group) >= 10:
            raise GroupLimitError(f"Не можна додати більше 10 студентів у групу {self.number}")
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = ""
        for student in self.group:
            all_students += str(student) + "\n"
        return f"Number:{self.number}\n{all_students}"


# ===== ТЕСТИ =====
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')


# ===== ДЕМОНСТРАЦІЯ: перехоплення винятку при 11-му студенті =====
try:
    # Додамо ще 8 студентів (щоб стало рівно 10)
    for i in range(3, 11):
        gr.add_student(Student('Male', 20 + i, f'Name{i}', f'Last{i}', f'RB{i}'))

    print("У групі вже 10 студентів.")

    # Спроба додати 11-го
    gr.add_student(Student('Female', 19, 'Extra', 'Student', 'RB11'))

except GroupLimitError as e:
    print("Помилка додавання:", e)
