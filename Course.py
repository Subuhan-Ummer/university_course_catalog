#base class
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours


    def display_info(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}"


#subclass for core course
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_info(self):
        core_info = super().display_info()
        return f"{core_info}, Required for Major : {self.required_for_major}"


#subclass for elective course
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_info(self):
        elective_info = super().display_info()
        return f"{elective_info}, Elective Type : {self.elective_type}"


core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective_course = ElectiveCourse("ENG202", "Creative Writing", 2, "Liberal arts")

print(core_course.display_info())
print(elective_course.display_info())