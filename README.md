# university_course_catalog

This project is a Python-based University Course Catalog Management System. It defines a base class, `Course`, and two subclasses, `CoreCourse` and `ElectiveCourse`, to represent different types of university courses.

## Table of Contents

- [Overview](#overview)
- [Classes and Structure](#classes-and-structure)
- [Usage](#usage)

---

## Overview

The University Course Catalog program is an object-oriented system for managing university courses. The `Course` class provides shared attributes for all courses, while `CoreCourse` and `ElectiveCourse` extend the functionality for specific course types.

## Classes and Structure

- **Course**: Base class with attributes:
  - `course_code` (str): Unique code for the course (e.g., "CS101")
  - `course_name` (str): Name of the course (e.g., "Introduction to Computer Science")
  - `credit_hours` (int): Number of credit hours for the course

- **CoreCourse**: Subclass of `Course` with an additional attribute:
  - `required_for_major` (bool): Indicates if the course is required for a major

- **ElectiveCourse**: Subclass of `Course` with an additional attribute:
  - `elective_type` (str): Specifies the type of elective (e.g., "general", "technical", "liberal arts")

## Usage

1. Create instances of `CoreCourse` and `ElectiveCourse` and call the `display_info()` method to view course details.

   ```python
   # Example usage
   core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
   elective_course = ElectiveCourse("ENG202", "Creative Writing", 2, "liberal arts")

   print(core_course.display_info())
   print(elective_course.display_info())
