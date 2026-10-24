# ⚡ Hogwarts Playground OOPS Engine

[![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)](https://www.python.org/)

A terminal-based simulator built to practice and solidify my Object-Oriented Programming (OOP) principles in Python. This project models the Hogwarts ecosystem to experiment with software architecture, state management, and strict typing. 

---

## 🧠 Core Concepts Demonstrated

* **Encapsulation:** Utilized `@property` decorators and private variables to safely manage state (e.g., binding a student's energy strictly between 0 and 100).
* **Inheritance:** Built a robust base `Wizard` class inherited by specialized `Student` and `Professor` child classes.
* **Polymorphism:** Overrode the `duel()` method, allowing students and professors to execute entirely different combat logic using the exact same method signature.
* **Abstraction:** Implemented Python's `ABC` (Abstract Base Classes) to enforce strict contracts, guaranteeing all child classes of `MagicalEntity` define an `interact()` method.
* **Class Methods:** Leveraged `@classmethod` as alternative factory constructors (e.g., a Sorting Hat mechanism) and class variables to track global states.

---

## 📂 Project Structure

```text
hogwarts_engine/
├── models/
│   ├── academics.py    # Subject and House models
│   ├── creatures.py    # Abstract MagicalEntity and Creature models
│   └── people.py       # Wizard, Student, and Professor models
├── database.py         # In-memory seeder bridging objects and relationships
└── main.py             # Master controller and interactive CLI

```

---

## 🚀 Usage

Clone the repository and run the main controller to launch the interactive terminal interface:

```bash
git clone [https://github.com/Divya4879/hogwarts_engine.git](https://github.com/Divya4879/hogwarts_engine.git)
cd hogwarts_engine
python main.py

```
---

**CLI Features:**

* View live House standings and academic rosters.
* Initiate dynamic, polymorphic duels between characters.
* Enter the Forbidden Forest to test encapsulated energy damage against magical creatures.
