class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_bonus(self, bonus_rate):
        return self.salary * bonus_rate


# ---- TEST THE CLASS ----

emp = Employee("John Doe", 50000)

print("Employee:", emp.name)
print("Salary:", emp.salary)

bonus_rate = float(input("Enter bonus rate (example 0.10 for 10%): "))

bonus = emp.get_bonus(bonus_rate)

print("Bonus amount:", bonus)
