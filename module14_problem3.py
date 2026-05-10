class Student:

    # tuition rate dictionary
    rates = {
        "I": 250,
        "O": 500,
        "X": 800,
        "G": 250
    }

    def __init__(self, first_name, last_name, district, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district = district
        self.credits = credits

    def calculate_tuition(self):

        rate = Student.rates[self.district]
        return self.credits * rate


# ---- TEST ALL TYPES ----

student1 = Student("Jane", "Doe", "I", 12)
student2 = Student("John", "Smith", "O", 12)
student3 = Student("Liu", "Wang", "X", 12)
student4 = Student("Alex", "Brown", "G", 12)

students = [student1, student2, student3, student4]

for s in students:
    print("\nStudent:", s.first_name, s.last_name)
    print("District:", s.district)
    print("Credits:", s.credits)
    print("Tuition owed:", s.calculate_tuition())
