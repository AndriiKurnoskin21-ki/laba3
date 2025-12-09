# Лаба 3 – Введення студентів та оцінок через input()

students = {}  # словник: ім'я -> оцінка

print("Введи ім'я студента та його оцінку. Для завершення введи 'stop'.")

while True:
    name = input("Ім'я студента: ")

    if name.lower() == "stop":
        break

    grade = int(input("Оцінка студента (1-12): "))
    students[name] = grade


# --- Виведення всіх студентів ---
print("\n=== Список студентів та їх оцінок ===")
for name, grade in students.items():
    print(f"{name}: {grade}")


# --- Обчислення статистики ---
grades = list(students.values())

if grades:  # якщо список не пустий
    average = sum(grades) / len(grades)
else:
    average = 0

# Категорії
excellent = [name for name, g in students.items() if 10 <= g <= 12]
good = [name for name, g in students.items() if 7 <= g <= 9]
bad = [name for name, g in students.items() if 4 <= g <= 6]
failed = [name for name, g in students.items() if 1 <= g <= 3]


# --- Виведення статистики ---
print("\n=== Статистика ===")
print(f"Середній бал по групі: {average:.2f}")

print(f"Кількість відмінників (10–12): {len(excellent)} — {excellent}")
print(f"Кількість хорошистів (7–9): {len(good)} — {good}")
print(f"Кількість відстаючих (4–6): {len(bad)} — {bad}")
print(f"Кількість тих, хто не здав (1–3): {len(failed)} — {failed}")
