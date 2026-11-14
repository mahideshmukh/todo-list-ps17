# To-Do List Application (PS 17)

**Name:** Mahi Deshmukh | **ERP No.:** 01429

**Rungta International Skills University** | School of Computer Science and Engineering
**Programme:** B.Tech Computer Science and Engineering
**Language:** Python 3 | **Concepts:** Lists, Functions, Loops, File Handling

## Problem Statement

Develop a menu-driven to-do list where a user can add tasks, view all tasks, mark a task as completed and delete a task. Tasks are saved to `todo.txt` after every change. Task numbers start from 1 and every new task starts as Pending.

## Features

- Add a task (empty titles are rejected)
- View all tasks with number, title and status
- Mark a task as completed
- Delete a task
- Tasks are loaded from `todo.txt` at start and saved after every change
- A missing `todo.txt` is handled safely
- Loop-driven menu with an Exit option

## How to Run

```
python todo.py
```

## Program Structure

| Function | Purpose |
|---|---|
| `load_tasks()` | Reads tasks from `todo.txt` |
| `save_tasks(tasks)` | Writes all tasks to `todo.txt` |
| `get_task_number(tasks)` | Asks for a task number and validates it |
| `add_task(tasks)` | Adds a new Pending task |
| `view_tasks(tasks)` | Prints all tasks |
| `complete_task(tasks)` | Marks a task as Done |
| `delete_task(tasks)` | Removes a task |
| `main()` | Runs the menu loop |

## Test Cases

| # | Input | Expected Output |
|---|---|---|
| 1 | Option 1 (Add), Task: Buy books | Task added. 1 \| Buy books \| Pending |
| 2 | Empty list, Option 2 (View) | No tasks found. Your to-do list is empty. |
| 3a | Option 3 (Complete), task number 5 | Task number 5 not found. |
| 3b | Option 1 (Add), Task: (empty) | Task title cannot be empty. |
| 4a | Option 3 (Complete), task 1 | Task 1 marked as completed. |
| 4b | Option 2 (View) | 1 \| Buy books \| Done and 2 \| Pay bill \| Pending |
| 4c | Option 4 (Delete), task 2 | Task 2 deleted. Tasks left: 1 |
## Test Case Output

Output of the program for each test case (run with `python todo.py`).

### Test Case 1: Normal Input
```
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 1
Task: Buy books
Task added. 1 | Buy books | Pending

1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 5
Goodbye!
```

### Test Case 2: Boundary / Minimum Input
```
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 2
No tasks found. Your to-do list is empty.

1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 5
Goodbye!
```

### Test Case 3: Invalid Input

(a) Complete with task number 5 (only 1 task exists)

```
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 3
Task number: 5
Task number 5 not found.

1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 5
Goodbye!
```

(b) Add with an empty task title

```
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 1
Task:
Task title cannot be empty.

1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 5
Goodbye!
```

### Test Case 4: Different Valid Scenario

Tasks: 1 Buy books, 2 Pay bill. Then Complete 1, View, Delete 2.

```
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 1
Task: Buy books
Task added. 1 | Buy books | Pending

1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 1
Task: Pay bill
Task added. 2 | Pay bill | Pending

1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 3
Task number: 1
Task 1 marked as completed.

1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 2
1 | Buy books | Done
2 | Pay bill | Pending

1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 4
Task number: 2
Task 2 deleted. Tasks left: 1

1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 2
1 | Buy books | Done

1. Add  2. View  3. Complete  4. Delete  5. Exit
Choose option: 5
Goodbye!
```