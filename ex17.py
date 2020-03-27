from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Копирование данных из файла {from_file} в файл {to_file}.")

#можете следующие две строки кода разместить в одну
in_file = open(from_file)
indata = in_file.read()

print(f"Исходный файл имеет размер {len(indata)} байт.")

print(f"Целевой файл существует? {exists(to_file)}.")
print("готов, нажмите клавишу enter для продолжения или CTRL+C для отмены.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("отлично, все сделано.")

out_file.close()
in_file.close()
