# 1. Python Modules and Data Handling Assignment
# Objective:
# The aim of this assignment is to assess your understanding and ability to implement Python modules, both built-in and custom, and to apply data handling techniques using Python's data structures and error handling. This assignment will help solidify your grasp on creating and using modules, as well as manipulating and processing data effectively in Python.

# Task 1: Your Mood Today

# Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today and responds with a custom message based on the mood entered.
from mood import Mood

if __name__ == "__main__":
    mood_instance = Mood()
    mood_instance.mood_input()