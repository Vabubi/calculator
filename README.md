# Calculator Project


#### Project Description

This is an object-oriented Python calculator that performs basic mathematical operations while maintaining a memory state. The calculator supports addition, subtraction, multiplication, division, root extraction, and memory reset.


### Features:

__Addition (add(n))__
Adds a number n to the current memory value.

__Subtraction (subtract(n))__
Subtracts a number n from the current memory value.

__Multiplication (multiply(n))__
Multiplies the current memory value by n.

__Division (divide(n))__
Divides the current memory value by n. Includes error handling for division by zero.

__Root Extraction (root(n))__
Takes the nth root of the current memory value.

__Memory Reset (reset())__
Resets the memory back to 0.0.


# How to Use:

    1. Clone the repository

    git clone:

    https://github.com/Vabubi/calculator_project.git

    2. Navigate to the project directory

    cd calculator_project

    3. Run the Calculator

    python -m calculator.calculator


# Running Tests:

    1. Install pytest (if not installed)

    2. pip install pytest

    3. Run the tests

    pytest tests/test_calculator.py


# Project Structure:

· calculator_project/

    .gitignore
    README.md
    setup.py

· calculator/

    __init__.py
    calculator.py

· tests/

    test_calculator.py

· calculator

Contains the core functionality (calculator.py) and an init.py to define it as a package.

· tests

Houses test_calculator.py, which contains the unit tests for all calculator methods.

·  .gitignore

Specifies files/folders to be excluded from version control.

·  README.md

Provides an overview and instructions for using the project.

· setup.py

Allows the calculator to be installed as a Python package if desired.

Author:
Created by Jokūbas
