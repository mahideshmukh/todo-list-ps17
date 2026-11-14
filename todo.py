FILE = "todo.txt"


def load_tasks():
	"""File se tasks padho. File na mile to empty list do."""
	tasks = []
	try:
		with open(FILE, "r") as f:
			for line in f:
				line = line.strip()
				if "|" in line:
					title, status = line.rsplit("|", 1)
					tasks.append([title, status])
	except FileNotFoundError:
		pass
	return tasks


def save_tasks(tasks):
	"""Har change ke baad file mein save karo."""
	with open(FILE, "w") as f:
		for title, status in tasks:
			f.write(f"{title}|{status}\n")


def get_task_number(tasks):
	"""Task number maango aur check karo ki valid hai ya nahi."""
	num = input("Task number: ").strip()
	if num.isdigit() and 1 <= int(num) <= len(tasks):
		return int(num)
	print(f"Task number {num} not found.")
	return None


def add_task(tasks):
	title = input("Task: ").strip().replace("|", " ")
	if title == "":
		print("Task title cannot be empty.")
		return
	tasks.append([title, "Pending"])
	save_tasks(tasks)
	print(f"Task added. {len(tasks)} | {title} | Pending")


def view_tasks(tasks):
	if len(tasks) == 0:
		print("No tasks found. Your to-do list is empty.")
		return
	for i, (title, status) in enumerate(tasks, start=1):
		print(f"{i} | {title} | {status}")


def complete_task(tasks):
	num = get_task_number(tasks)
	if num is None:
		return
	tasks[num - 1][1] = "Done"
	save_tasks(tasks)
	print(f"Task {num} marked as completed.")


def delete_task(tasks):
	num = get_task_number(tasks)
	if num is None:
		return
	tasks.pop(num - 1)
	save_tasks(tasks)
	print(f"Task {num} deleted. Tasks left: {len(tasks)}")


def main():
	tasks = load_tasks()
	while True:
		print("\n1. Add  2. View  3. Complete  4. Delete  5. Exit")
		choice = input("Choose option: ").strip()
		if choice == "1":
			add_task(tasks)
		elif choice == "2":
			view_tasks(tasks)
		elif choice == "3":
			complete_task(tasks)
		elif choice == "4":
			delete_task(tasks)
		elif choice == "5":
			print("Goodbye!")
			break
		else:
			print("Invalid option.")


main()
