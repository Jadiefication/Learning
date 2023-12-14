from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk

# University interface
class UniversityInterface(ABC):

  @abstractmethod
  def add_course(self, course_name):
    pass

  @abstractmethod
  def enroll_student(self, student, course_name):
    pass

  @abstractmethod
  def hire_professor(self, professor, course_name):
    pass

  @abstractmethod
  def print_stats(self):
    pass


# University and related classes  
class University(UniversityInterface):

  def __init__(self, name, location):
    self.name = name
    self.location = location
    self.courses = {}

  def add_course(self, course_name):
    self.courses[course_name] = []

  def enroll_student(self, student, course_name):
    if course_name in self.courses:
      self.courses[course_name].append(student)

  def hire_professor(self, professor, course_name):
    if course_name in self.courses:
      self.courses[course_name].append(professor)

  def print_stats(self):
    print(f"University: {self.name}")
    print(f"Location: {self.location}")
    print("Courses:")
    for course, people in self.courses.items():
      print(f"- {course}: {len(people)} people")


class Student:

  def __init__(self, name, year):
    self.name = name
    self.year = year


class Professor:

  def __init__(self, name, department):
    self.name = name
    self.department = department


# GUI
class UniversityGUI:

  def __init__(self, master):
    self.master = master
    self.uni = University("Python University", "Boston")

    # Frames
    courses_frame = ttk.LabelFrame(master, text="Courses")
    courses_frame.grid(row=0, column=0, padx=10, pady=10)

    students_frame = ttk.LabelFrame(master, text="Students")
    students_frame.grid(row=0, column=1, padx=10, pady=10)

    professors_frame = ttk.LabelFrame(master, text="Professors")  
    professors_frame.grid(row=0, column=2, padx=10, pady=10)

    # Course widgets
    courses_label = ttk.Label(courses_frame, text="Add Course:")
    courses_label.grid(row=0, column=0)
    
    self.courses_entry = ttk.Entry(courses_frame)
    self.courses_entry.grid(row=0, column=1)
    
    add_course_btn = ttk.Button(courses_frame, text="Add Course", command=self.add_course)
    add_course_btn.grid(row=0, column=2)

    # Student widgets
    name_label = ttk.Label(students_frame, text="Student Name:")    
    name_label.grid(row=0, column=0)
    
    self.name_entry = ttk.Entry(students_frame)
    self.name_entry.grid(row=0, column=1)
    
    enroll_btn = ttk.Button(students_frame, text="Enroll", command=self.enroll_student)
    enroll_btn.grid(row=0, column=2)

    # Professor widgets
    
    # Styling
    style = ttk.Style()
    style.theme_use("clam")

  def add_course(self):
    course_name = self.courses_entry.get()  
    self.uni.add_course(course_name)

  def enroll_student(self):
    name = self.name_entry.get()
    student = Student(name, "Freshman")
    self.uni.enroll_student(student, "Python 101")
    

root = tk.Tk()
app = UniversityGUI(root)
root.mainloop()