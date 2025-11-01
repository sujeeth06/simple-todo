<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Project-Simple_ToDo_List-brightgreen?style=flat-square" alt="Project">
</p>

<h1 align="center">📝 Simple To-Do List (Python CLI)</h1>

<p align="center">
  A beginner-friendly Python project to manage daily tasks in your terminal.<br>
  Save, view, and delete your tasks easily with persistent storage!
</p>

---

## 🚀 Features
- ✅ Add new tasks  
- 📋 View all saved tasks  
- 🗑️ Delete tasks by number  
- 💾 Tasks auto-save in `tasks.txt`  
- 💻 Simple and beginner-friendly CLI interface

---

## 🧠 How It Works
1. When you run the program, it checks for a file named `tasks.txt`.
2. All tasks are loaded from that file (if it exists).
3. You can add, view, or delete tasks using the menu.
4. The updated tasks list is automatically saved.

---

## 🗂️ Project Structure
simple-todo/
│
├── simple_todo.py        # main Python file
├── tasks.txt             # stores your tasks (auto-created)
├── README.md             # project documentation
└── requirements.txt      # optional (no external packages needed)