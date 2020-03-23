types_of_people = 10
x = f"Существует {types_of_people} типов людей"

binary = "python"
do_not = "нет"
y = f"те кто понимает {binary}, и те кто - {do_not}."

print(x)
print(y)

print(f" Я сказал: {x}")
print(f'а еще сказал: "{y}"')

hilarious = False
joke_evaluation = "Разве это не смешно?! {}"

print(joke_evaluation.format(hilarious))

w = "Это часть строки слева..."
e = "а это справа."

print(w + e)