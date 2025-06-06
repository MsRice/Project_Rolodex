# 🧩 Sudoku Validator

A command-line Sudoku validator written in Python. This project takes a completed 9x9 Sudoku puzzle input from the user, validates its structure, and checks whether it satisfies all Sudoku rules:

- Each row must contain digits 1–9 without repetition.
- Each column must contain digits 1–9 without repetition.
- Each 3×3 sub-grid must contain digits 1–9 without repetition.

---

## 🎯 Objectives

This project was designed to improve skills in:

- Handling user input
- Manipulating strings and lists
- Implementing logic to validate grid-based puzzles

---

## 📋 Features

- Validates input length and content
- Checks Sudoku rules for rows, columns, and 3x3 sub-squares
- Provides success or failure feedback
- Includes sample test boards

---

## 🚀 How to Use

1. Clone or download this repository:

    ```bash
    git clone https://github.com/your-username/sudoku-validator.git
    cd sudoku-validator
    ```

2. Run the program:

    ```bash
    python sudoku_validator.py
    ```

3. Follow the prompt to enter 81 digits (9 rows of 9 numbers). Example:

    ```
    Enter 9 rows of 9 digits:
    295743861431865927876192543387459216612387495549216738763524189928671354154938672
    ```

4. You'll receive a message indicating whether your Sudoku is valid or not.

---

## 🧪 Sample Input & Output

    [2,9,5,7,4,3,8,6,1],
    [4,3,1,8,6,5,9,2,7],
    [8,7,6,1,9,2,5,4,3],
    [3,8,7,4,5,9,2,1,6],
    [6,1,2,3,8,7,4,9,5],
    [5,4,9,2,1,6,7,3,8],
    [7,6,3,5,2,4,1,8,9],
    [9,2,8,6,7,1,3,5,4],
    [1,5,4,9,3,8,6,7,2]

    Victory! Sudoku conquered.



