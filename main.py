# Python Modules 2 and 3 Practice Project

import random
import calculator


# Exercise 3: Simple Class and Inheritance

print("=== Student Information ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


student = Student("Alex", 22, "ST123")
student.greet()
print("Student ID:", student.student_id)


# Exercise 4: Math Quiz with Exception Handling

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)

print("\nMath Quiz")
print("What is", number1, "+", number2, "?")

try:
    answer = int(input("Your answer: "))

    if answer == number1 + number2:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", number1 + number2)

except ValueError:
    print("Invalid input!")


# Exercise 8: Simple Calculator Module

print("\nSimple Calculator")

try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        result = calculator.add(first_number, second_number)
    elif operation == "-":
        result = calculator.subtract(first_number, second_number)
    elif operation == "*":
        result = calculator.multiply(first_number, second_number)
    elif operation == "/":
        result = calculator.divide(first_number, second_number)
    else:
        result = None
        print("Invalid operation.")

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
