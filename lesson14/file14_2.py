# ===== КАСТОМНИЙ ВИНЯТОК =====
class GroupLimitError(Exception):
    """Виняток, якщо в групі більше 10 студентів"""
    pass


# ===== БАЗОВИЙ КЛАС =====
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


# ===== СТУДЕНТ =====
class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.record_book})"

    # Для assert gr.find_student('Jobs') == st1
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return str(self) == str(other)

    # Щоб Student можна було класти у set
    def __hash__(self):
        return hash(str(self))


# ===== ГРУПА =====
class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if student not in self.group and len(self.group) >= 10:
            raise GroupLimitError(
                f"Не можна додати більше 10 студентів у групу {self.number}"
            )
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
        students = "\n".join(str(s) for s in self.group)
        return f"Number:{self.number}\n{students}"


# ===== ТЕСТИ З УМОВИ =====
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student


# ===== ПЕРЕВІРКА ВИНЯТКУ (11-й студент) =====
try:
    for i in range(3, 12):
        gr.add_student(Student('Male', 20 + i, f'Name{i}', f'Last{i}', f'RB{i}'))
except GroupLimitError as e:
    print("Виняток перехоплено:", e)
