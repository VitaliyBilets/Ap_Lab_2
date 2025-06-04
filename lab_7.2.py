from lab_7 import rabin_karp
import os
folder_path = "txt"
needle = input("Введіть шаблон  ")


for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()
            positions = rabin_karp(text, needle)

            print(f"\n Файл: {filename}")
            if positions:
                print(f"Знайдено шаблон  {positions}")
            else:
                print(" Шаблон не знайдено.")