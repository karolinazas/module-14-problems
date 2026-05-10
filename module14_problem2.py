class Student:

    def __init__(self, first_name, last_name, district, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district = district
        self.credits = credits

    def calculate_tuition(self):

        if self.district == "I":
            rate = 250
        else:
            rate = 500

        return self.credits * rate


# ---- TEST THE CLASS ----

student1 = Student("Jane", "Doe", "I", 12)

print("Student:", student1.first_name, student1.last_name)
print("District:", student1.district)
print("Credits:", student1.credits)

tuition = student1.calculate_tuition()

print("Tuition owed:", tuition)
