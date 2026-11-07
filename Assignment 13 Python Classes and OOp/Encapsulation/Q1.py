# Q1 - Student Result Manager (Encapsulation)

class Student:
    def __init__(self, name, marks):
        self.name = name                 # Public attribute
        self._marks = 0                  # Protected attribute
        self.__grade = None              # Private attribute
        self.set_marks(marks)

    def set_marks(self, marks):
        if isinstance(marks, bool) or not isinstance(marks, (int, float)) or not 0 <= marks <= 100:
            print("Invalid marks: enter a number from 0 to 100.")
            return False

        self._marks = marks
        self.__grade = None              # Recalculate grade when requested
        print("Marks updated successfully.")
        return True

    def get_marks(self):
        return self._marks

    def get_grade(self):
        if self._marks >= 80:
            self.__grade = "A"
        elif self._marks >= 60:
            self.__grade = "B"
        elif self._marks >= 40:
            self.__grade = "C"
        else:
            self.__grade = "F"
        return self.__grade


if __name__ == "__main__":
    student1 = Student("Ali", 85)
    student2 = Student("Sara", 55)

    print(f"{student1.name}: marks={student1.get_marks()}, grade={student1.get_grade()}")
    print(f"{student2.name}: marks={student2.get_marks()}, grade={student2.get_grade()}")

    student1.set_marks(92)       # Valid update
    student2.set_marks(120)      # Invalid update

    print(f"{student1.name}: marks={student1.get_marks()}, grade={student1.get_grade()}")

    # Extension: direct access to __grade is not available by its original name.
    try:
        print(student1.__grade)
    except AttributeError:
        print("Direct access to __grade is blocked (name-mangled by Python).")
