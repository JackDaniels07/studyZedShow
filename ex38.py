ten_things = "Яблоки Апельсины вороны Телефоны Свет Сахар"

print("Погодитеб тут меньше 10 объектовю Давай это исправим.")

stuff = ten_things.split(" ")
more_stuff = ["День", "Ночь", "Песня", "Мишка", "Кукуруза", "банан", "Девочка", "Мальчик"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print("add: ", next_one)
    stuff.append(next_one)
    print(f"Теперь у нас есть {len(stuff)} объектов.")
    
print("Итак: ", stuff)

print("Давайте кое что сделаем с нашим объектоми.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print('\n'.join(stuff))
print('#'.join(stuff[3:5]))