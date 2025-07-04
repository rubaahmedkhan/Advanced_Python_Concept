# 📘 Advanced Python Concepts - Theoretical Notes

This README contains **deep theoretical explanations** of important advanced Python topics. All corresponding code is hosted in this repository. Use this document to refresh your concepts anytime.

---

## 📌 1. `@dataclasses`

- Introduced in Python 3.7 via `dataclasses` module.
- Reduces boilerplate code required to create classes that store data.
- Automatically generates methods like `__init__`, `__repr__`, `__eq__`, etc.
- Great for creating **immutable** or **mutable** data containers.

### Key Features:
- Type annotations are used to define fields.
- `frozen=True` makes the dataclass immutable.
- `default_factory` allows dynamic default values.

>  Use case: Configuration classes, DTOs (Data Transfer Objects)

---

## 📌 2. Metaclasses

- **Classes of classes** – They define how classes behave.
- Just like a class creates an object, a metaclass creates a class.
- You can customize class creation, modify class attributes/methods dynamically.

### How it works:
- Python uses `type` as the default metaclass.
- You can create a custom metaclass by inheriting from `type`.
- Override `__new__` and `__init__` methods to control class construction.

>  Use case: Enforcing coding standards, automatic registration of classes, ORM model generation

---

## 📌 3. Decorators

- A **higher-order function** that takes a function/class and returns a modified version.
- Used to **modify behavior without changing the original code**.
- Syntax: `@decorator_name`

### Types:
- **Function Decorators** – Modify function behavior.
- **Class Decorators** – Modify class-level functionality.
- **Built-in decorators**: `@staticmethod`, `@classmethod`, `@property`

>  Use case: Logging, authentication, memoization, performance tracking

---

## 📌 4. Duck Typing

- "If it walks like a duck and quacks like a duck, it's a duck"
- Python is **dynamically typed**, so types are not enforced explicitly.
- Focus is on **behavior, not inheritance**.
  
### Benefits:
- Enables **polymorphism** without inheritance.
- Promotes flexible and reusable code.

>  Use case: Any place where multiple object types with similar interfaces are used

---

## 📌 5. Association in OOP

- Describes **"has-a"** relationships between classes.
- One class **uses** another as part of its functionality.

### Types of Association:

#### 🔹 Aggregation
- **Weak association**.
- Child can exist **independently** of the parent.
- Example: Department has Teachers, but Teachers can exist without the Department.

#### 🔹 Composition
- **Strong association**.
- Child **cannot exist** independently of the parent.
- Example: House has Rooms. If House is destroyed, so are the Rooms.

>  Use case: Modeling real-world relationships (e.g., Company & Employees)

---

## 📌 6. Generics

- Allow code to be **type-safe and reusable** using templates.
- In Python, supported via the `typing` module (e.g., `List[int]`, `Dict[str, Any]`).
- `TypeVar` allows the creation of **generic functions or classes**.

### Key Concepts:
- `TypeVar` to declare placeholders.
- Helps with static type checking.

>  Use case: Creating reusable data structures like Stack, Queue, etc.

---

## 📌 7. Singleton Pattern

- Ensures that a **class has only one instance** and provides a global point of access to it.
- Used where exactly **one object is needed** to coordinate actions.

### Implementation Strategies:
- Override `__new__` method.
- Use metaclass to control instantiation.
- Use modules (since Python modules are singleton by default).

>  Use case: Logger, configuration manager, database connection pool

---

## 📦 Summary Table

| Concept         | Core Idea                              | Use Case                            |
|----------------|-----------------------------------------|-------------------------------------|
| Dataclasses     | Auto-generates boilerplate in classes   | DTOs, config data                   |
| Metaclasses     | Custom class creation                   | Code enforcement, ORMs              |
| Decorators      | Modify behavior without changing code   | Logging, permissions, caching       |
| Duck Typing     | Type by behavior                        | Polymorphism without inheritance    |
| Association     | Object relationships ("has-a")          | System modeling                     |
| Generics        | Reusable, type-safe structures/functions| Collections, custom data types      |
| Singleton       | One instance only                       | Logging, DB connections             |

---


