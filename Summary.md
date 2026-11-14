# Project Summary: To-Do List Application (PS 17)

**Name:** Mahi Deshmukh | **ERP No.:** 01429
**Programme:** B.Tech Computer Science and Engineering, Rungta International Skills University

## Objective

To build a menu-driven to-do list in Python 3 where a user can add tasks, view all tasks, mark a task as completed and delete a task. Tasks are saved to `todo.txt` after every change.

## Approach

- The whole program is in one file, `todo.py`.
- Tasks are held in a Python list. Each task is stored as `[title, status]`, where status is `Pending` or `Done`.
- A `while True` loop shows the menu (Add, View, Complete, Delete, Exit) until the user chooses Exit.
- One function is written for each action: `add_task`, `view_tasks`, `complete_task` and `delete_task`.
- `load_tasks()` reads `todo.txt` when the program starts. If the file is missing, the program starts with an empty list.
- `save_tasks()` writes all tasks back to `todo.txt` after every change.
- `get_task_number()` checks that the task number is a valid number within the list.

## Concepts Used

| Concept | Where it is used |
|---|---|
| Lists | Storing all tasks |
| Functions | One function per feature |
| Loops | Menu loop, reading and writing the file |
| File handling | Loading and saving `todo.txt`, handling a missing file |
| Validation | Empty task title, invalid task number |

## Test Results

All 4 test cases from the problem statement give the expected output.

| Test Case | Result |
|---|---|
| 1. Normal input (add a task) | Pass |
| 2. Boundary input (view an empty list) | Pass |
| 3. Invalid input (task number 5 not found, empty title) | Pass |
| 4. Different valid scenario (complete, view, delete) | Pass |

The detailed output of each test case is in `README.md`.

## Conclusion

The program meets all the minimum requirements of the problem statement: a single `.py` file, a list-based store with a loop-driven menu and Exit option, one function each for add, view, complete and delete, file persistence in `todo.txt`, and validation of the task title and task number.

## Files in this Repository

- `todo.py`: the complete program
- `README.md`: documentation, program structure, test cases and their output
- `SUMMARY.md`: this summary