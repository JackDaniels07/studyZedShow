from sys import argv

script, filename = argv

print(f"Я собираюсь стереть файл {filename}.")rint("если вы не хотите стирать его, нажмите CTRL+C (^C).")
print("Если хотите стереть файл, нажмите клавишу Enter.")
input("?")

print("Щткрытие файла...")
target = open(filename, 'w')

print("Очистка файла. Досвидания")
target.truncate()

print("Теперь я запрашиваю у Вас 3 строки.")

line1 = input("строка 1: ")
line2 = input("строка 2: ")
line3 = input("строка 3: ")

print("Это я запишу в файл.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("И наконец, я закрою файл.")
target.close()
